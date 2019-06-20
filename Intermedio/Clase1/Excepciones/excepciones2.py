#Bloque try:
try:
	x = 10/0

#Se ejecuta el bloque except si se realiza una división entre cero.
except ZeroDivisionError:
	print("La división entre 0 no es posible.")
#Se ejecuta si no cacha la excepcion
else:
	print(x)