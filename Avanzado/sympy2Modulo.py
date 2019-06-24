#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 24 09:48:39 2019

@author: arianafm
"""

from sympy import pi, E, oo, cos
#E : Euler
#oo : Infinito
radio = 5
#Sin el evalf la operación queda expresada únicamente.
area = pow((pi.evalf()*radio),2)
print(area)
#5**3
print(E.evalf())
print(oo.evalf())

# V A R I A B L E S  S I M B Ó L I C A S
#a
#Símbolos
x = Symbol('x')
y = Symbol('y')
print(x)
print(y)
#Muchos símbolos a la vez
a,b,c = symbols('a,b,c')
print(a,b,c)

#Te devuelve una tupla que va desde q hasta w
variables = var('q:w')
print(variables)

#Ecuación general
ecuacion = x+y
print(ecuacion)

#Solución particular
#Le diste valor a x
sol_par = ecuacion.subs(x,3)
print(sol_par)
