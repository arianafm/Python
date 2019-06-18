archivo = open("mi_archivo.txt","a")
#La a hace referencia a append para que de ese modo empiece a escribir desde donde se quedo el archivo.

archivo.write("Esta es la línea de prueba.")
archivo.close()

archivo = open("mi_archivo.txt","a")
archivo.write("\nEsta es otra línea de prueba.")