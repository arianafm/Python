#Función normal:

def f(x):
	resultado = x**2
	return resultado

print(f(3))

#Lambda:

#Le podemos asignar una variable a la función.
aux = lambda x: x**2
print(aux(5))

#También podemos hacerlo de la siguiente manera:
#Donde separamos (Función lambda)(parámetro)
print((lambda x: x**4)(2))

#Tarea opcional:
#Cómo usar condicionales en una lambda y usarlo con la serie de Fibonacci.

