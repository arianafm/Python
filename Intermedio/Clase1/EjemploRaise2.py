#Raise: invoca excepciones de Python.
while True:

	mejorCurso = input("Ingresa cuál es el mejor curso de Proteco:")

	mejorCursoConMinusculas = mejorCurso.lower()

	if mejorCursoConMinusculas != "python am sala a":
		raise ValueError
	else:
		print("Felicidades, Python AM sala A es el mejor curso.")
		break