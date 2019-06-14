#Escribe una función que cuente el número de vocales en una cadena dada.
contador = 0

def vocales(a):
	global contador
	for x in a:
		if (x == "a") or (x == "e") or (x == "i") or (x == "o") or (x == "u"):
			contador += 1
	print(contador)

cadena = input("Ingresa una cadena:")
vocales(cadena)

