#Dada una lista de cadenas de diferentes longitudes, crear una función que tome como entrada dicha lista y la devuelva ordenada de la cadena más pequeña a la más larga.

#zip(): mapea el índice similar de múltiples contenedores 
#		para que puedan usarse como una sola entidad.

from operator import itemgetter

#Lista inicial.
lista = ["ariana","gloria","donaldo","jose"]

def numeroCaracteres(l):
	valores = []
	for x in range(len(l)):
		contador = len(l[x])
		valores.append(contador)
	return valores


def creandoDiccionario(llaves,valores):
	dicc = dict(zip(llaves,valores))
	return dicc

#Lista de longitudes de las cadenas de la lista inicial.
listanum = numeroCaracteres(lista)
#Diccionario creado a partir de la lista inicial y la lista de longitudes.
dicc = creandoDiccionario(lista,listanum)
#Diccionario ordenado por valores (de menor a mayor).
diccsort = dict(sorted(dicc.items(), key=itemgetter(1)))
#Obtenemos las llaves de nuestro diccionario ordenado.
claves = list(diccsort.keys())
#Regresamos la lista ordenada de la cadena más pequeña a la más larga.
print(claves)
