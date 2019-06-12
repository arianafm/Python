#Variable global.
numero = 20
print(numero)

def prueba():
	#Variables globales y locales.
	#En variable global, número vale 20.
	#En variable local, cambiamos el valor de "número" a 15.

	#Mandamos a llamar a la variable global.
	global numero
	#Variable local.
	numero = 15
	print(numero)

prueba()
print(numero)