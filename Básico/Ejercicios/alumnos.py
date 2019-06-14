"""
Ejercicio:

1.- Lista de objetos de la clase Alumno.
2.- Alumno tendrá:
		- Nombre
		- Apellidos
		- Cuenta o matrícula
		- Nombre de las materias (5)
		- Calificaciones (5)
		- Promedio
3.- Se debe poner ingresar todos los datos a través de la terminal hasta que el 
	usuario escriba: "Salir".
"""

class Alumno:

	def __init__(self ,nombre ,apellido, cuenta, calificaciones, promedio):
	
		self.nombre = nombre
		self.apellido = apellido
		self.cuenta = cuenta
		self.materias = []
		self.calificaciones = []
		self.promedio = promedio

	Menu = True

	while Menu:
		print("Menú")
		print("1.- Nombre.")
		print("2.- Apellidos.")
		print("3.- Inserta número de cuenta.")
		print("4.- Inserta tus materias.")
		print("5.- Inserta tus calificaciones.")
		print("6.- Conoce tu promedio.")
		print("7.- Salir")

		num = int(input("Seleccione una opción:"))

		if num == 1:
			nombre = input("Inserta nombre del alumno:")

		elif num == 2:
			apellido = input("Inserta apellidos del alumno:")

		elif num ==3:
			cuenta = input("Inserta apellidos del alumno:")




