"""
Hacer una calculadora:
-Suma
-Resta
-Multiplicación
-División
En caso de que el usuario ingrese una división entre 0 debe preguntarte:
¿Deseas realizar otra operación?
"""
def suma(a,b):
	print(a+b)

def resta(a,b):
	print(a-b)

def multi(a,b):
	print(a*b)

def div(a,b):
	print(a/b)


while True:
	print("-"*20 + " CALCULADORA " + "-"*20)
	print("1.- Suma.")
	print("2.- Resta.")
	print("3.- Multiplicación.")
	print("4.- División.")
	print("5.- Salir.")
	num = int(input("Seleccione una opción:"))

	if num == 1:
		sum1 = int(input("Ingresa el primer número:"))
		sum2 = int(input("Ingresa el segundo número:"))
		suma(sum1,sum2)
	elif num == 2:
		res1 = int(input("Ingresa el primer número:"))
		res2 = int(input("Ingresa el segundo número:"))
		resta(res1,res2)
	elif num == 3:
		mul1 = int(input("Ingresa el primer número:"))
		mul2 = int(input("Ingresa el segundo número:"))
		multi(mul1,mul2)
	elif num == 4:
		div1 = int(input("Ingresa el primer número:"))
		div2 = int(input("Ingresa el segundo número:"))
		try:
			div(div1,div2)
			break
		except ZeroDivisionError:
			print("La división entre 0 no es posible.")
			continuar = input("¿Desea realizar otra operación?")
			if continuar == "si" or continuar == "Si":
				continue
			elif continuar == "no" or continuar == "No":
				break
			else:
				print("---------ERROR-------")

	elif num ==5:
		print ("Hasta pronto.")
		break