#Asignar valores por defecto.

def hola(a=5,b=6):
	print("La suma es: ",a+b)

# * Desempaque, te regresa el valor.
def argumentos(*galileo):
	for x in galileo:
		print(x)

# ** Desempaca los dos valores del diccionario es decir: llave y valor.
def diccionarios(**diccio)
	#Notemos las dos variables en el for...
	#Items regresa llave y valor.
	for x,y in diccio.items():
		print(x + " : "+y)

hola()
hola(2,3)
argumentos(6,"hola",7,"mamamia","python")
diccionarios(nombre = "Aldo", edad = "21", dinero = "mucho", comer="verdura")