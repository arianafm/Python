#G E N E R A D O R E S

#Devuelven un objeto iterable.
#Se definen igual que las funciones pero en vez de utilizar la palabra "return" 
#utiliza la palabra "yield".
#Generan datos en tiempo de ejecución.

def generador():
	yield "hola"
	yield "adiós"
	yield 1
	yield (3,3)

a = generador()

#Next corresponde a un método mágico.
#Con next mandas a llamar a los miembros dentro de generador.
print(a.__next__())
print(a.__next__())
print(a.__next__())
print(a.__next__())

#En caso de que no haya más elementos y volviesemos a usar el método mágico nos lanzaría un error.

#Generador de números pares:
#n - Me ayuda a saber cuántos números pares me faltan
#a - Me ayuda a saber si el número es par o no
def pares(n):
	a = 0
	while n>0:
		if a%2 == 0:
			yield a
			n = n-1
		a+=1

#Para recorrer un iterable puedes usar un for:
for num in pares(10):
	print(num)