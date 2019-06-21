import socket

socketCliente = socket.socket()

#socketCliente.connect(("localhost",3000))
#En vez de localhost ponemos la dirección IP del servidor.
#Direcciín IP del servidor y puertos.
socketCliente.connect(("192.168.3.13",9000))

while True:
	mensaje = input("Ingrese tu mensaje:")
	#Como nosotros escribimos mensajes, nosotros debemos modificar.
	#Mandar nuestro mensaje de String a bytes.
	socketCliente.send(mensaje.encode())
	if mensaje == "adios":
		break

socketCliente.close()