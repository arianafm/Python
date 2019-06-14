x = [1,2,3,4]
y = ["Uno","Dos","Tres"]

listavarios = [5,2.4,"Dos",[1,2,[4,"hola"]]]
numeroDeElementos = len(x)

print(numeroDeElementos)

#I N D I C E S
#Recuerda empezar a contar desde 0.

#Te metes al índice 0 de la lista.
print(x[0])
#Te metes al índice 1 de la lista y al índice 1 de la cadena.
print(y[1][1])
print(listavarios[3][2][1][0])
#Comienzas contando desde el último elemento.
print(x[-2])

#Manipulación de listas 
#Cambiar el valor de los índices en x
x[0] = 10
print(x)

#Agregando el elemento al final de la lista
y.append("Cuatro")
print(y)

#Agregando el elemento en dónde queramos
y.insert(0, "Nuevo dato")
print(y)

# M E T O D O S  P A R A  E L I M I N A R
#Eliminar por coincidencia
x.remove(10)
print(x)

#Eliminar por índice
del y[0]
print(y)