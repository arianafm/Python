#H E R E N C I A:
#La herencia nos permite reutilizar código.

"""
class Persona:

	def __init__(self,nombre,apellido,edad):

		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad

	def saludar(self):

		print("{nombre} dice hola.".format(nombre=self.nombre))

class Vegetarianos:

	def __init__(self,nombre,apellido,edad):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad

	def saludar(self):

		print("{nombre} dice hola.".format(nombre=self.nombre))

	def comer(self):

		print("Lo sientooooo, no como carne.")

"""

class Persona:

	def __init__(self,nombre,apellido,edad):

		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad

	def saludar(self):

		print("{nombre} dice hola.".format(nombre=self.nombre))

#Heredamos de otra clase de la siguiente manera:
#Aquí vegetariano hereda de persona.
class Vegetariano(Persona):

	def comer(self):

		print("Lo sientooooo, no como carne.")

aldo = Vegetariano("Aldo","Vázquez",21)
aldo.saludar()
aldo.comer()