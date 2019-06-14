# D I C C I O N A R I O S

x = {}
x['red'] = "el color rojo"
x['green'] = "el color verde"
print(x)

#Quiero imprimir en pantalla "el color rojo"
print(x['red'])
#Llenando diccionario en una sola línea de código.
y = {"red":"el color rojo","green":"el color verde"}
print(y)
#Diccinario de varios tipos de dato
y = {"uno": 1, 2: "dos", 2.5: "numero flotante", "lista":[2,3,4,"hola"], (1,2,3): "una tupla"}

print(y[(1,2,3)])
print(y[2.5])
#Reemplazamos "[2,3,4,"hola"]"" con "mundo".
y["lista"] = "mundo"
print(y)

#Recuperando las llaves
#Obtienes solamente las llaves.
claves = y.keys()
print(claves)

#Convertimos las llaves a una lista.
aux=list(claves)
print(aux)


#Recuperando los valores de las llaves.
#Obtienes solamente los valores.
valores = y.values()
print(valores)

#Convertimos las valores a una lista.
aux2=list(valores)
print(aux2)

#Buscando los valores
#Regresa un booleano: en caso de encontrarlo regresa True en caso contrario False.
print("dos" in valores)

print("-------------------")

#Borrando
#Borra la llave y con ella se borra el elemento.
del y ["uno"]
print(y)
#Borra el diccionario.
del y
print(y)
#Borraste el diccionario y después lo mandaste a imprimir.
#Como el diccionario ya no existe te sale el siguiente error...
"""
Traceback (most recent call last):
  File "diccionarios.py", line 51, in <module>
    print(y)
NameError: name 'y' is not defined
"""