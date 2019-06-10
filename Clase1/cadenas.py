#Cadenas
#Una línea 
x = 'Hola mundo'
#Cadenas de varias líneas
x = ''' Cadena
de
varias
líneas '''
#print(x)

#Concatenación de cadenas
x = 'Hola'
y = ' mundo'
z = x + y
print(z)

#Multiplicación con cadenas 
w = x*10
print(w)

#Método split
#Separa las cadenas cuando encuentra el carácter indicado.
#En este caso 'a'.
y = "Hola-Mundo-Otra-Palabra"
x = y.split('a')
print(x)

#Método join
#Concatena las cadenas usando - (en este caso) entre ellas.
x = "-".join(["Junta", "las", "palabras"])
print(x)

#Método find
#Encuentra coincidencias.
a = "ferrocarril"
posicion = a.find("rr")
print(posicion)

#Formatos de impresión de cadenas
numero = 3
numero2 = 5
resultado = numero + numero2
print("El primero número es:", numero, "El segundo número es:",numero2, "El resultado de sumar ambos numeros es:", resultado)

#Otra manera:
print("El número: %f"%(numero))

#Método format
print("El curso de {pythonam} es mejor que {pythonpm}".format(pythonam="Rodrigo", pythonpm="Héctor"))

#Lectura de valores por teclado
#Lo que recibe input lo hace em formqa cadena-string
a = input("Ingresa algo:")
print("Hola", a)







