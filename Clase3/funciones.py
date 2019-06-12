#Funciones en Python:
import math

def saludar():
	print("Hola.")

def suma(a,b):
	resultado = a+b
	print("La suma es:", resultado)
	return resultado

def formulaGeneral(a,b,c):
	if a == 0:
		print("La división entre 0 está indefinida.")
		return None, None
	elif b**2-4*a*c < 0:
		print("Hay raíces complejas.")
		return None, None
	else:
		res1 = (-b+math.sqrt(b**2-4*a*c))/(2*a)
		res2 = (-b-math.sqrt(b**2-4*a*c))/(2*a)
		return res1,res2

saludar()
x = suma(3,8)
r1 , r2 = formulaGeneral(1,2,1)

print("Estoy fuera de la función y el resultado es",x)
print("La primer raíz es:", r1)
print("La segunda raíz es:", r2)
