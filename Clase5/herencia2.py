#Agreguemos otra clase a nuetro código.

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

#Agreguemos una tercera clase y esta heredará de la segunda.
class Vegano(Vegetariano):

	def saludar(self):

		print("Hola soy {nombre} y soy vegano.".format(nombre=self.nombre))

	def comer(self):

		print("Yo no como ningún producto animal. ¿Ya mencioné que soy vegano?")

aldo = Vegetariano("Aldo","Vázquez",21)
aldo.saludar()
aldo.comer()

rodrigo = Vegano("Rodrigo","Vivas",23)
rodrigo.saludar()
rodrigo.comer()