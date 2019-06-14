#D E C O R A D O R E S

#Se trata de una función que recibe como parámetro otra función y devuelve una función.
#Sirve para agregar más acciones a nuestra función.

def agregar(funcion):
	def decorar():
		print("Está apunto de iniciar mi función.")
		funcion()
		print("Terminó la ejecución.")
	return decorar

#Decorar: @nombreDeFunción
#Cuando mandas a llamar hola, también llamas a la función agregar (esto para decorar).
#Otra notación en lugar de @agregar() es: 
#agregar(hola)()
@agregar
def hola():
	print("Hola")

hola()
