class Persona:

	planeta = "Tierra"

	def __init__(self ,nombre ,apellido ,edad):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.habilidades = []

	#Sobreescribimos el método 
	def __str__(self):

		return self.nombre + " " + self.apellido

	def __add__(self, otra_persona):
		return self.edad + otra_persona.edad

	def __len__(self):
		return len(self.habilidades)


aldo = Persona("Aldo","Vázquez",21)
rodrigo = Persona("Rodrigo","Vivas",23)
#Imprime la dirección en memoria del objeto.
#<__main__.Persona object at 0x108480da0>
#Cada objeto tiene un método predeterminado ___str__(self)
print(aldo)
print(aldo + rodrigo)
print(len(aldo))
