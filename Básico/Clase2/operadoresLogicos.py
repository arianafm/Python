#Comparaciones múltiples con operadores lógicos.

#OR / "o":

#NOT/ "no":
x = int(input("Ingrese un número:"))

# "%" Operador módulo: Regresa el residuo de la división entre dos números.
if x%2!=0: #1,3,5,7...
	print("El número {0} es impar.".format(x))

if x%3==0 or x%5==0: #3,5,6,9,10,15...
	print("El número {0} es divisible entre 3 o entre 5.".format(x))

#El operador lógico "not" va junto al if y sólo recibe un parámetro.
if not x%5==0: #1,2,3,4,6,7...
	print("El número {0} no es divisible entre 5.".format(x))
