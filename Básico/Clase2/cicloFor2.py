#Declaramos las dos listas
lista1 = [1,2,3]
lista2 = [4,5,6]

for x in lista1:
	for y in lista2:
		#Imprime 
		print(x,y) 

#Función range:

#Imprime del [1, 10) es decir, del 1 al 9 ya que hace un iterable de ese tamaño.
for x in range(1,10):
	print(x)

#Condiciones:
for x in range(1,10,2):
	#Imprime 1,3,5,7,9 es decir cada dos elementos.
	print(x)