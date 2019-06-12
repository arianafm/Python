#Paso por valor 
"""
Unicamente se manda una copia de mi variable principal a la función.
Esto ocurre con tipos de dato simples.
Enteros, flotantes.
"""

n=10

def duplicar(parametro):
	parametro = parametro*2
	print(parametro)

print("-"*30)
print(n)
print("-"*30)
duplicar(n)
print("-"*30)
print(n)

#Paso por referencia
"""
Se manda la variable y sus datos son modificados en la función
"""
lista = [2,3,4]

def duplica(l):
	for x in range(len(l)):
		l[x] = l[x]*2
		print(l[x])

print("-"*30)
print(lista)

#La copia tiene otra dirección de memoria, entonces NO se modifica la lista inicial.
#Otra notación para copy es ... lista[:]
duplica(lista.copy())

#Mostrando que la lista inicial NO fue modificada.
print(lista)