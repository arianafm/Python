class Alumno:

	def __init__(self,nombre,apellido,cuenta,materias,calificaciones):

		self. nombre = nombre
		self. apellido = apellido 
		self. cuenta = cuenta
		self. materias = materias 
		self. calificaciones = calificaciones 
		self. promedio = sum(self.calificaciones)/5

	#Los métodos (self) irán a la altura del constructor.
	def __str__(self):
		return "El alumno {alumno} tiene {promedio} de promedio".format(alumno=self.nombre,promedio=self.promedio)

#Las funciones deberán ir identadas así.
def leer_calificaciones():
	calificaciones = []
	for iterador in range(5):
		calificacion = float(input("Ingrese la calificación:"))
		calificaciones.append(calificacion)
	return calificaciones

def leer_materias():
	materias = []
	for iterador in range(5):
		materia = input("Ingrese la materia:")	
		materias.append(materia)
	return materias

			

alumnos = []

while True:
	opcion = input("¿Desea agregar otro alumno? / Escriba salir para terminar el programa:")
	if opcion == "salir":
		break
	else:
		nombre = input("Ingrese el nombre:")
		apellido = input("Ingrese el apellido:")
		cuenta = input("Ingrese el número de cuenta:")
		materias = leer_materias()
		calificaciones = leer_calificaciones()

		alumno = Alumno(nombre,apellido,cuenta,materias,calificaciones)
		alumnos.append(alumno)

		for alumno in alumnos:
			print(alumno)
