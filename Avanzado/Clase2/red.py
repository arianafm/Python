# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 11:01:56 2019

@author: cur01alu31
"""
#Modelo de una red neuronal

"""
Compuerta AND
Entradas	Salidas
0  0			0
0  1			0
1  0			0
1  1			1
"""

#Mi primer perceptrón:
import random
import time

def funcion_activacion(x1,x2,w1,w2,b):
	operacion = (x1*w1 + x2*w2)-b
	if operacion >= 0:
		return 1
	else:
		return 0

#Valores con los que ira probando
entradas = [(0,0),(0,1),(1,0),(1,1)]
#Los que queremos ontener.
salidas = [0,0,0,1]

w1 = 0.5
w2 = 0.2
b = 0.24
eta = 0.25

#Hace el for para encontar la salida,
i = 0
for x in range(32):
	#Entre más veces que lo hagas más veces mejora.
	if i == 4:
		i = 0
		time.sleep(2)
		print()
	#Entradas:
	x1 = entradas[i][0]
	x2 = entradas[i][1]
	#Salida deseada:
	D = salidas[i] #Este valor obtenido es igual a ...
	Y = funcion_activacion(x1,x2,w1,w2,b) 
	#print() que indica el estado actual de las variables:
	print("x1 = {0} x2 = {1} D = {2} Y = {3} w1 = {4} w2 = {5}".format(x1,x2,D,Y,w1,w2))

	#Cálculo de error:
	delta = D-Y
	d1 = eta * delta * x1
	d2 = eta * delta * x2

	w1 += d1
	w2 += d2

	#Bias
	b = b-eta * delta
	i += 1





