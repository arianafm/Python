#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 25 09:36:10 2019

@author: arianafm
"""
from sklearn.datasets import load_iris
from sklearn import tree
import numpy

iris = load_iris()

#Obteniendo datos que se usarán como prueba:
#Setosa -> 0
prueba_target = iris.target[0] #El dato 0 es una setosa.
prueba_data = iris.data[0]

#Antes de entrenar a nuestro algoritmo le quitaremos tres datos.
#PRIMER ARGUMENTO
#De que conjunto eliminarás los datos
#SEGUNDO ARGUMENTO
#Índices a borrar del conjunto

#De los datos queremos borrar una fila:
#Se eliminan con axis = 0, si no podría tomarlo como columna.
target = numpy.delete(iris.target, [0,50,100] )
data = numpy.delete(iris.data, [0,50,100] , axis = 0)

clasificador = tree.DecisionTreeClassifier()

clasificador = clasificador.fit(data, target)

print("Datos de prueba:")
print(prueba_target)
print(prueba_data)
#Como ya puse una lista dentro de una lista, ya es de dos dimensiones y por eso funciona.
print(clasificador.predict([prueba_data])) #El resultado es [0] lo que indica setosa.
#Primer parámetro:
#Largo del cepalo
#Segundo parámetro:
#Ancho del cepalo
#Tercer parámetro:
#Largo del pétalo
#Cuarto parámetro:
#Ancho del pétalo
print(clasificador.predict([[4,2,1,1.5]])) #A veces sale 0, a veces 1...
#Generalmente en los algoritmos como fit tratan de seguir la misma ruta pero en puede no tomarla.

