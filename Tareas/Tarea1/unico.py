#Dada una lista de números ordenados (de forma creciente) en la cual todos los 
#números, excepto uno, aparecen duplicados, realiza un programa que encuentre 
#el número que no está duplicado dentro de la lista.

#Ejemplo:
#Dada la lista: [1, 1, 3, 3, 4, 5, 5, 6, 6, 7, 7], el programa devuelve 4.

# min(): devuelve el elemento con el valor más bajo.
lista = [1, 1, 3, 3, 4, 5, 5, 6, 6, 7, 7]

dicc = {}

for x in lista:
	if x in dicc.keys():
		dicc [x] += 1
	else:
		dicc[x] = 1

#print(dicc)
#{1: 2, 3: 2, 4: 1, 5: 2, 6: 2, 7: 2}


minimo = min(dicc, key=dicc.get)

print(minimo)

