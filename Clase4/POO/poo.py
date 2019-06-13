class Persona:

	#Método init: Construye nuestro objeto.
	#init es el método contructor.
	#Se definirá todo lo que nuestra nueva instancia contendrá como caracteristicas.

	#Self es referencia al objeto.
	def __init__(self ,nombre ,apellido ,edad):
		#Característica del objeto = nombre que le pasamos como parámetro.
		self.nombre = nombre
		self.apellido = apellido
		#Objeto tiene edad y su edad es la que le estás pasando.
		self.edad = edad

	def saludar(self):
		print("{nombre} dice : ¡Hola!".format(nombre = self.nombre))
#Instancia de persona:
#Aquí se manda a llamar a init y se le pasan los parámetros que serán la caracteristica de nuestro objeto.
aldo = Persona("Aldo","Vázquez",21)
#El objeto creado manda a llamar al método saludar.
aldo.saludar()

"""
En caso de poner únicamente saludar() sin aldo.saludar() saldría este error:
Traceback (most recent call last):
  File "poo.py", line 13, in <module>
    saludar()
NameError: name 'saludar' is not defined
Cuba31:POO cur01alu31$ 
"""
