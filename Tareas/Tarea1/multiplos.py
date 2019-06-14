#Función que recibe dos números como parámetros e indica si el primer número es múltiplo 
#del segundo.
#Se ejecuta en el flujo principal y pide los números al usuario.

def multiplos(a,b):
	resultado = a % b
	if resultado == 0:
		print("Los números", a, "y", b, "son múltiplos.")
	else:
		print("Los números", a, "y", b, "no son múltiplos.")

num1 = int(input("Ingresa el primer número:"))
num2 = int(input("Ingresa el segundo número:"))
multiplos(num1,num2)





