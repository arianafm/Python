#Aquí declaramos nuestra propia excepcion que herede de la clase Exception.

class miExcepcion(Exception):

	def __init__(self, mensaje):
		self.mensaje = mensaje


def unaFuncion(param = None):
	if param == None:
		raise miExcepcion("Mi excepcion ha sido invocada.")

unaFuncion()

"""
Lo que nos arroja la terminal es:
Traceback (most recent call last):
  File "MiDeclaracionDeExcepciones.py", line 13, in <module>
    unaFuncion()
  File "MiDeclaracionDeExcepciones.py", line 11, in unaFuncion
    raise miExcepcion("Mi excepcion ha sido invocada.")
__main__.miExcepcion: Mi excepcion ha sido invocada.
"""
