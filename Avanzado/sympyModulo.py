#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:38:41 2019

@author: arianafm
"""
from sympy import *
#Forzar tipos de datos
#Hacer casting
entero = 5
transformacion = Float(entero)
print(transformacion)

#Rational te pide numerador y denominador
fraccion = Rational(1,2)
fraccion2 = Rational(3,8)
entreCero = Rational(4,0)
suma = fraccion + fraccion2
print(suma)
print(entreCero) #Imprime: zoo = complex infinity
