try:
	x = 10/0
#inst será nuestra variable.
except ZeroDivisionError as inst:
	print(type(inst)) #La instancia de la excepcion
	print(inst.args) #Imprimir los argumentos guardados en .args
	print(inst) #__str__ permite imprimit directamente los argumentos
	
	