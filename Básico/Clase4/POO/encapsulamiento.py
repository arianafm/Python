class Persona:

	def __init__(self ,nombre ,apellido ,edad):
	
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		self.habilidades = []
		#Como está privado te dirá que no tiene. ***
		self.__telefono = "55555555"

	def get_telefono(self):

		return self.__telefono

	def set_telefono(self,nuevo_numero):
		self.__telefono = nuevo_numero


aldo = Persona("Aldo","Vázquez",21)
#Usando un get ya es posible acceder a un atributo privado.
print(aldo.get_telefono())
#aldo.__telefono = "33333333" ERROR: No puedes modificar así un atributo privado.
#Así se modifica un atributo privado:
aldo.set_telefono("5534056152")
print(aldo.get_telefono())

"""
***
ERROR EN LA TERMINAL
***
Traceback (most recent call last):
  File "encapsulamiento.py", line 12, in <module>
    print(aldo.__telefono)
AttributeError: 'Persona' object has no attribute '__telefono'
"""