while True:
	cadena = input("Ingrese una cadena: ")
	if cadena == "salir":
		#break rompe con nuestro ciclo.
		break

	if cadena == "continuar":
		#Ignora el código que siga dentro del ciclo pero
		#regresa y ejecuta el principio.
		continue

	if cadena == "pasar":
		#Pasas hasta que ya sepas que poner.
		pass

	print("Tu cadena es:"+cadena)
