"""
Declaramos nuestra excepcion que herede la clase Exception
y debemos sobreescribir el método main y que el mensaje sea 
"No puedes retirar dinero negativo."
Hacemos una función que pida al usuario un valor, si el valor es negativo debemos mandar a llamar a nuestra función con raise.
Vaya, si el valor ingresado es < 0 mandas a llamar la excepcion que creaste.
"""

class excepcion(Exception):
	def __init__(self, mensaje):
		self.mensaje = mensaje

def unaFuncion(param = None):
	if param == None:
		raise excepcion("No puedes retirar dinero negativo.")

while True:
	print("___CAJERO___")
	print("1.- Retirar dinero")
	print("2.- Salir")
	op = int(input("Seleccione una opción:"))

	if op == 1:
		cantidad = int(input("Ingrese la cantidad que desea retirar:"))
		if cantidad <= 0 :
			unaFuncion()
		else:
			print("Cantidad retirada.")
			print("Hasta pronto.")
			continuar = input("¿Desea retirar otra cantidad?")
			if continuar == "si" or continuar == "Si":
				continue
			elif continuar == "no" or continuar == "No":
				break
			else:
				print("---------ERROR-------")
	elif op == 2:
		print("Hasta pronto.")
		break
	else:
		print("Opción inválida.")


		