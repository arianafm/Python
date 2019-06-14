#Elabora un programa que sea capaz de calcular el IMC (Índice de masa corporal) de una persona. Los datos deberán ser ingresados por el usuario.

#Información necesaria:
#Peso en kg.
#Estatura en m².

#Fórmula del IMC usando el sistema métrico:
#Peso dividido por la estatura al cuadrado.

peso = float(input("Ingrese su peso en kg:"))
estatura = float(input("Ingresa su estatura en m²:"))

def formulaIMC(a,b):
	if (a <= 0) or (b <=0):
		print("ERROR")
		print("Ninguno de los datos ingresados puede tomar valores menores o iguales a cero.")
	else:
		potEstatura = (estatura**2)
		resultado = peso/potEstatura
		print("Su índice de masa corporal es:", resultado)

formulaIMC(peso,estatura)

"""
Ejemplo:

Altura: 165 cm 
		ó
		1.65 m

Peso: 68 kg

Cálculo: 68 ÷ (1.65)² = 
		 68 ÷ (2.7225) = 24.977043158861342

"""





