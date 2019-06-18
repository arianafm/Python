#Expresiones regulares.

#Secuencia especial de caracteres que ayuda a encontrar otras cadenas o conjuntos de cadenas utilizando una sintáxis mantenida en un patrón.

import re #re: Regular expression.

#Si la cadena coincide (es decir hace match) regresa un objeto de tipo match, y si no, regresa None.
#Parámetro izquierdo: Expresión regular. (Secuencia de carácteres)
#Parámetro derecho: Cadena a comparar.

if re.match("hola","hola"):
	print("Hizo match.")

#Este también hace match porqué le importa que haga match con lo que debe, lo demás no le importa.
if re.match("hola","holat"):
	print("Hizo match 1.")

#Match verifica la coincidencia  al INICIO de la cadena.
if re.match("hola","ko hola"):
	print("Hizo match 2.")

#. Compara con cualquier carácter.
if re.match(".ola","tola"):
	print("Hizo match 3.")

#.... En mi cadena tendré cuatro carácteres, los que sean.
if re.match("....","tola"):
	print("Hizo match 4.")

#\ tomalo como lo que es y no como un metacaracter
#\ antidiagonal es un caracter de escape.
if re.match("\.ola","hola"):
	print("Hizo match 5.")

#Sirve para poner varias opciones:
if re.match("(p|j|c)ython","python"):
	print("Hizo match 6.")

if re.match("(pyy|j|c)ython","pyyython"):
	print("Hizo match 7.")

if re.match("niñ(o|a)s","niñas"):
	print("Hizo match 8.")

"""
[0-9] -> Obtiene un carácter del 0 al 9.
[a-z] -> Carácter de la a a la z.
[A-Z] -> Carácter de la A a la Z.
[0-9a-zA-Z] -> Carácter dentro del rango de letras may. y min. y numéricos.
[a-f0-5]
"""

if re.match("cadena[0-9]","cadena0"):
	print("Hizo match 9.")

if re.match("cadena[0-9]","cadena1"):
	print("Hizo match 10.")

if re.match("cadena[0-9]","cadena1s"):
	print("Hizo match 11.")

#Negación ^
#Carácter diferente a lo que se encuentre en ese rango.
if re.match("python[^0-9a-z]","pythonA"):
	print("Hizo match 12.")

"""
Cuantificadores:
+, *, ?, {}

+ -> El carácter que precede existe 1 o más veces.
* -> El carácter que precede existe 0 o más veces.
? -> El carácter que precede puede existir o no (1 o 0 veces).
{n} -> n = número de veces exactas que queremos que aparezca el carácter.

"""

if re.match("python+","pythonnnnn"):
	print("Hizo match 13.")

if re.match("python*","pytho"):
	print("Hizo match 14.")

if re.match("py(tho)?n","pythothon"):
	print("Hizo match 15.")

if re.match("py(tho)?n","pyn"):
	print("Hizo match 16.")

if re.match("pyth{3}on","pythhhon"):
	print("Hizo match 17.")

if re.match("pyth{3,5}on","pythhhhhon"):
	print("Hizo match 18.")

"""
^ -> Debe ir al principio de la cadena.
$ -> Debe ir al final de la cadena.
"""

if re.match("^(http|https)","google.com"):
	print("Hizo match 19.")

if re.match("^(http|https)","http://google.com"):
	print("Hizo match 20.")

#Le decimos que debe acabar con .com
if re.match("com$","google.com"):
	print("Hizo match 21.")

"""
\d -> Equivale [0-9]
\D -> Equivale [^0-9]
\w -> Equivale [a-zA-Z_]
\W -> Equivale [^a-zA-Z_]
#Incluye también el carácter _
"""

"""
Tarea:
Crear expresión regular para detectar correos.
"""

