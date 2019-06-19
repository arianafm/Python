import re

try:
	archivo = open("correos.txt","r")
	contenido = archivo.read()
	print("Los correos electrónicos encontrados son:")
	expresion = re.compile("[A-Za-z0-9\.-_]+@[A-Za-z0-9\.-_]+\.[A-Za-z0-9]+")
	#.* Cualquier caracter cualquiera alfanumérico.
	coincidencias = expresion.findall(contenido)
	print(coincidencias)
	archivo.close()
except FileNotFoundError:
	print("No se encontro el archivo con ese nombre.")


"""
".+[a-zA-Z]+\..*[com|mx]"
En este caso, antes del @ podría haber lo que sea, por eso nos arroja todo.
"""

"""
"[\w\.-_]+@[\w\.-_]+\.[\w]+"
Puede ser que \w también englobe al @
"""

