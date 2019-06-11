#Ciclos iterativos.

#Importando una función de un módulo para dormir el proceso.
from time import sleep 

#While

#Contador
x = 0

#Ciclo while
while x<10:
	print("Este código se está ejecutando por {0} vez".format(x))
	x = x+1
	#Sleep recibe como parámetro el número de segundos que tardará dormido.
	sleep(2)