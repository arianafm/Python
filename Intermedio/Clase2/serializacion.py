#Serialización: estándar para manejar formatos.
#Por ejemplo formatos json o csv.
#La serialización se encarga de convertir  los json o los csv en formatos
#que podemos manejar fácilmente.
import json
#Valores y llave.
#Los json son como los diccionarios de los archivos.

#json.dump() y json.load()

archivo_json = open("clase.json","r")
diccionario = json.load(archivo_json)
print(diccionario)

diccionario["estatura"] = 1.70
habilidades = diccionario["habilidades"]
habilidades.append("Bailar")
print(diccionario)
archivo_json.close()

archivo_json = open("clase.json", "w")
json.dump(diccionario,archivo_json,indent=4)

import csv
#Valores separados por coma.
#Los csv son como las listas de los archivos.

row = ["Rodrigo",23,"Vivas"]
archivo_csv = open("clase.csv","w")

# csv.reader() y csv.writer()

#Writer:
#Primero convierte en lista y te permite ir agregando rows, append a la lista.
#No necesita poner append y no sobreescribe.
salida = csv.writer(archivo_csv)
salida.writerow(row)
row = ["Aldo",21,"Vázquez"]
salida.writerow(row)

archivo_csv.close()
archivo_csv = open("clase.csv","r")
#Reader:
#Convierte csv en lista.
lector = csv.reader(archivo_csv)
for row in lector:
	print(row)