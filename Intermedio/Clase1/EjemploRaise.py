#Raise: invoca excepciones de Python.

mejorCurso = input("Ingresa cual es el mejor curso de proteco:")

if mejorCurso != "Python AM sala A.":
	raise Exception
else:
	print("Felicidades, Python AM sala A es el mejor curso.")

"""
En caso de poner algo diferente a "Python AM sala A.":
La terminal te devuelve:
Ingresa cual es el mejor curso de proteco: probando
Traceback (most recent call last):
  File "EjemploRaise.py", line 6, in <module>
    raise Exception
Exception
"""

