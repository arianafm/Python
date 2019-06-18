"""
Ejercicio:

	Desarrollar un sistema para supermercado.
	El usuario agregará productos al carrito (nombre, cantidad) Hasta que escriba salir.
	El supermercado obtendrá los precios e imprimirá el ticket para el usuario en formato txt.
"""

class Producto():
	def __init__(self, nombre, precio):

		self.nombre = nombre
		self.precio = precio

	def __str__(self):
		return "Producto:{pro} \nPrecio:{pre}".format(pro=self.nombre,pre=self.precio)

def recorre(productos,ticket):
	for x in productos:
		ticket.write(str(x)+"\n")


productos = []
ticket = open("mi_archivo.txt","w")
while True:
	opc = input("¿Desea agregar un producto?")
	if opc == "si":
		nombre = input("Nombre del producto:")
		precio = input("Precio del producto:")
		resultado = Producto(nombre,precio)
		productos.append(resultado)
	else:
		recorre(productos,ticket)
		break
