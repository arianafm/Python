#De lectura ponemos r de read (Archivo de tipo lectura)
archivo = open("ejemplo.txt","r")

#Sólo los tienen los .read (Es decir los archivos de tipo lectura))
print(archivo.read())

#Todos los archivos.py son de texto plano
#Si le pasaramos e1.py o algo asi

#archivo_salida = open("prueba_salida.txt","w")
archivo_salida = open("/Users/cur01alu47/Desktop/prueba_salida.txt","w")
archivo_salida.write("Esta es una prueba de escritura de archivo.")
#Para cerrar un acrhivo:
archivo_salida.close()
#Con esto cerrramos el flujo de datos.
archivo_salida = open("/Users/cur01alu47/Desktop/prueba_salida.txt","w")
#Lo volvemos a abrir y a escribir sobre él.
#Es como empezar de cero.
archivo_salida.write("Esta es otra.")

#Los archios en python se crean con este open no con os.
#Puedes poner la ruta que desees tipo:
#archivo_salida = open("/Users/cur01alu47/Desktop/prueba_salida.txt","w")

#Sólo los archivos de escritura se crean al momnto de que existen.
#Los de leer NO.
