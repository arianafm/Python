#Ejercicio de hacer un menú:
# -Ingresa opción
# -Sumar dos números
# -Elevar un número a la potencia n
# -Imprime los números pares del 1 al 100
# -Salir


Calculadora = True
bandera = True

while Calculadora:
	print("Menú")
	print("1.- Suma dos números.")
	print("2.- Elevar número a la potencia n.")
	print("3.- Mostrar números pares del 1 al 100.")
	print("4.- Salir")
	num = int(input("Seleccione una opción:"))

	if num == 1:
		sum1 = int(input("Ingresa el primer número:"))
		sum2 = int(input("Ingresa el segundo número:"))
		sumresul = sum1 + sum2
		print(sumresul)
		continuar = input("¿Deseas volver al menú?")
		if continuar == "si" or continuar == "Si":
			continue
		elif continuar == "no" or continuar == "No":
			break
		else:
			print("---------ERROR-------")
			break
	elif num == 2:
		pot1 = int(input("Ingresa el número:"))
		pot2 = int(input("Ingresa la potencia:"))
		potresul = pot1**pot2
		print(potresul)
		continuar = input("¿Deseas volver al menú?")
		if continuar == "si" or continuar == "Si":
			continue
		elif continuar == "no" or continuar == "No":
			break
		else:
			print("---------ERROR-------")
			break
	elif num ==3:
		lista1 = []
		lista2 = []
		for x in range(1,101,1):
			lista1.append(x)
		for y in lista1:
			if y%2 == 0:
				lista2.append(y)
		print(lista2)
		continuar = input("¿Deseas volver al menú?")
		if continuar == "si" or continuar == "Si":
			continue
		elif continuar == "no" or continuar == "No":
			break
		else:
			print("---------ERROR-------")
			break
	elif num ==4:
		print("Hasta luego.")
		break


