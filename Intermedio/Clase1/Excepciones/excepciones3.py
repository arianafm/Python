try:
	print(x) #Tratamos e imprimir la variable "x" que NO está definida.
except NameError:
	print("La variable x NO está definida.")
#Finally se ejecutará pase lo que pase.
finally:
	print("Hasta pronto.")