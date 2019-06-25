#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 08:46:31 2019

@author: arianafm
"""
import numpy as np
lista =[1,2,4]
tupla = (1,2,3)
vector = np.array([2,3,4,5])
vector2 = np.array([6,7,8,9])


print(lista)
print(tupla)
print(vector)

#Suma de vectores
suma = vector + vector2
print(suma)
#Producto punto
#Te devuelve un escalar.
productoPunto = vector.dot(vector2)
print(productoPunto)
#Creando matrices con el método array
matriz = np.array([[1,2,3],[4,5,6],[7,8,9]])
matriz2 = np.array([[1],[2],[3]])
print(matriz)
print(matriz2)
#Multiplicación de matrices usando array y método dot.
print(matriz.dot(matriz2))

#Array con un rango de valores
#Imprime arreglo de [0-9]
array1 = np.arange(10)
print(array1)
#Le dices inicio y fin [2-19]
array2 = np.arange(2,20)
print("\n",array2)
#Inicia en 4, final es el 20 y es cada 3
array3 = np.arange(4,20,3)
print(array3)

#Arreglos especiales
#Los arregla con flotante ( Es por eso que aparece un punto).
#Se pasan como parámetro una tupla para defninr la dimensión.
#[[1. 1.]
 #[1. 1.]]
unos = np.ones((2,2))
print(unos)

#Crea la matriz de ceros
ceros = np.zeros((3,5))
print(ceros)

#Imprimiría cuartos:
#[0.  0.2 0.4 0.6 0.8 1. ]
lins = np.linspace(0,1,6)
print(lins)


#Matriz diagonal
#Matriz identidad
diagonal = np.eye(3)
print(diagonal)

# M A T R I Z
#Transpuesta
#Cambia renglones por columnas
#1+10j es número complejo
matriz1 = np.matrix([[1,3,-5],[8,9,1+10j]])
print(matriz1.T)
#Hermitiana
print(matriz1.H)
#Inversa 
print(matriz1.I)
#Multiplicación
#La columna del primero debe ser igual renglon del segundo
matriz5 = np.matrix([[5,5,5,5],[6,6,6,6]]) #2x3
matriz6 = np.matrix([[4,4],[7,7],[8,8]]) #3x2
try:
    print(matriz5*matriz6)
except ValueError:
    #No cumple con la regla de multiplicación de matrices.
    print("El número de columnas de tu primer matriz debe ser igual al número de renglones del segundo")























