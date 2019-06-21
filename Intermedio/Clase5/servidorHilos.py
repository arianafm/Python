import threading
import socket 
#¿Qué es un socket?
#De forma muy sencilla es una computadora (con un servidor) que recibe información.

#Clase definida para crear hilos.
class HiloCliente(threading.Thread):
	def __init__(self, socketCliente):
		threading.Thread.__init__(self)
		self.socketCliente = socketCliente

	#Las acciones run las realiza unicamente el cliente.
	def run(self):
		#Qué hara el servidor con esos hilos que esta recibiendo
		while True:
			mensaje = self.socketCliente.recv(1024).decode()
			if mensaje == "adios":
				break
			print("Mensaje: {0} desde: {1}".format(mensaje,str(threading.current_thread())))

		self.socketCliente.close()

#Guarda todos los clientes:
hilos = []
socketServidor = socket.socket()
#Dirección IP y en qué puerto está.
socketServidor.bind("localhost",5000)
print("Esperando conexiones...")
socketServidor.listen(1)
	#Espera conexiones
	while True:
		try:
			socketServidor.settimeout(1)
			print("Esperando conexión...")
			#accept devuelve dos valores: socket y dirección IP
			socketCliente, direccion = socketServidor.accept()
			#Nos devuelve un objeto.
			print("Conectando desde: ", direccion[0])
		#Si se cansa de estar a la escucha...
		except socket.timeout:
			#Continuará esperando.
			print("Esperando...")
			continue

		#El cliente debemos convertirlo en un hilo... es por eso que en el init pasamos objeto de tipo socket.
		#Ahora cada cliente se comporta como un hilo.
		hilo = HiloCliente(socketCliente)
		hilos.append(hilo)
		#Iniciar la ejecución de ese hilo.
		hilo.start()
		#Para saber que hilos están conectados.
		print(hilos)

socketServidor.close()
