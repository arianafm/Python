#Con ayuda de diccionarios y listas, elabora un programa que simule una agenda de contactos. El programa debe preguntar al usuario si desea agregar un nuevo contacto a su agenda; si el usuario responde que sí, deberá pedir datos como “nombre” y “teléfono”; en caso contrario deberá mostrar todos los usuarios agregados en la agenda y termina la ejecución del programa.

#Simular agenda de contactos.
#Pregunta al usuario si desea agregar un nuevo contacto a su agenda.
#En caso de "Sí": deberá agregar nombre y teléfono
#En caso de "No": mostrará todos los usuarios agregados en la agenda y termina la ejecución.

listaNombres = []
listaTelefono = []

while True:
	print("Contactos:")
	print("¿Desea agregar un nuevo contacto?")
	string = input("Seleccione una opción:")

	if (string == "Sí") or (string == "Si") or (string == "si"):
		nombre = input("Agrega un nombre:")
		listaNombres.append(nombre)
		numero = input("Agrega un teléfono:")
		listaTelefono.append(numero)
		continue
	elif (string == "no") or (string == "No"):
		dicc = dict(zip(listaNombres,listaTelefono))
		print(dicc)
		break
	else:
		print(("*"*30) + "ERROR" +("*"*30))
		break