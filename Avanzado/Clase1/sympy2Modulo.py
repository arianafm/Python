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

#Sustituyendo otros símbolos
sol = ecuacion.subs(x,y)
print(sol)

#Múltiples sustituciones
p = Symbol('p')
ecuacion2 = x*2 + 5*y - p
print(ecuacion2)

aux = ecuacion2.subs([(x,1),(y,5),(p,x)])
print(aux)

#Solución de ecuaciones
e = (x**2) - 5
print(solve(e))

#Cálculo de límites
#Función, variable respecto a... valor al que tiende
print(limit(cos(x)/x , x,0))
print(limit(sin(x)/x , x,0))
#Calculando integral
#Función, (variable respecto a, limite superior, limite inferior)
print(integrate(x**3,(x,-1,1)))







