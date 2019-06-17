try:
	print(x) #Tratamos e imprimir la variable "x" que NO está definida.
except NameError:
	print("La variable x NO está definida.")
else:
	print("Algo más NO está funcionando.")