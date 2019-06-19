import socket
#Estamos hacienco una red
#Las ip dentro de una red son ip privadas
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
hostname = "localhost" #También se puede usr "127.0.0.1"
ip_address = socket.gethostbyname(hostname)

print("Servidor {0} ip: {1}".format(hostname,ip_address))

complete_address = (ip_address ,3000) 
#El segundo parámetro representa al puerto las ip completas llevan la forma xxx.xxx.xxx:puerto 

#bind significa enlazar:
#Es decir nos va a conectar a otra computadora.

sock.bind(complete_address)

sock.listen(1)
#Espera conexiones.
#Siempre escucha lo que entra, por eo tiene un ciclo infinito.


while True:

	print("Esperando cliente...")
	conexion, direccion_cliente = sock.accept()

	try:
		while True:
			print("Cliente desde: {0}".format(direccion_cliente))
			data = conexion.recv(64)
			if data:
				#Recibe bytes y lo imprimimos despues de convertirlo a string
				print(data.decode())
				#Contestamos con una cadena y essta la convertimos a bytes.
				respuesta = input(">> ")
				#Para que sepa que codificación estamos usando:
				#Pudo haber sido ASCII o utf
				respuesta_bytes = respuesta.encode("utf-8")#Como llega en bytes decodificamos para convertirlo a cadena y mandarlo a cliente.
				conexion.sendall(respuesta_bytes)
	except Exception as e:
			print(e)
			print("NO hay clientes disponibles.")
			break
	finally:
			conexion.close()