class Persona:


	#Atributos de clase:
	#Constante para todos los objetos que se creen. (O sea será el mismo.)
	#Para acceder a atributos: instancia.atributo
	planeta = "Tierra"

	def __init__(self ,nombre ,apellido ,edad):
		self.nombre = nombre
		self.apellido = apellido
		self.edad = edad
		#No es necesario que venga como parámeto pero entonces todos los objetos tendrán una lista de habilidades.
		#Podemos alterar los valores de un objeto (como en el caso del método aprender que llenas la lista de cada objeto con las habilidades de cada uno).
		self.habilidades = []

	def saludar(self):
		print("{nombre} dice : ¡Hola!".format(nombre = self.nombre))

	def saludar_a_otra_persona(self, otra_persona):
		print("{nombre} saluda a {otro}".format(nombre=self.nombre,otro=otra_persona.nombre))

	def aprender(self, nueva_habilidad):
		self.habilidades.append(nueva_habilidad)

	#Es un decorador
	#Equivalente a un método estático en Java.
	#Es decir es un método de la clase y no del objeto.
	@classmethod
	#Aquí el self toma el valor de la clase.
	def respirar(self):
		print("Todas las personas respiramos.")


aldo = Persona("Aldo","Vázquez",21)
aldo.saludar()
rodrigo = Persona("Rodrigo","Vivas",23)

#print(rodrigo.planeta)
#print(aldo.planeta)

#Aldo ejecuta la acción (toma el valor de self) y Rodrigo toma el valor de otra_persona
#self se refiere al valor que este al lado del punto.

#aldo.saludar_a_otra_persona(rodrigo)
#rodrigo.saludar_a_otra_persona(aldo)
aldo.aprender("Dar clases.")
aldo.aprender("Cocinar.")
rodrigo.aprender("Bailar salsa.")

print("Habilidades de Aldo: {habs}".format(habs=aldo.habilidades))
print("Habilidades de Rodrigo: {habs}".format(habs=rodrigo.habilidades))

Persona.respirar()