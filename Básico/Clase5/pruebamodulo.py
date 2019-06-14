#import modulo
#Importar una sóla función:
from modulo import areaCirculo
#Funcionará similar a la primera:
import modulo as mo


while True:
	# \n salto de línea.
	print("Cálculo de áreas: \n")
	# \t tab
	print("\t1.- Cuadrado.")
	print("\t2.- Triángulo.")
	print("\t3.- Círculo.")
	#Command+shift+d para copiar el último renglón.
	print("\t4.- Rectángulo.\n")
	opcion = int(input("Ingresa la opción que deseas:"))
	if opcion == 1:
		lado = int(input("Dame el lado:"))
		resultado = mo.areaCuadrado(lado)
		print(resultado)
	elif opcion == 2:
		base = int(input("Dame el base:"))
		altura = int(input("Dame el altura:"))
		#Como importamos modulo as mo mandamos a llamarlo así:
		print(mo.areaTriangulo(base,altura))
	elif opcion == 3:
		radio = int(input("Dame el radio:"))
		#Como hicimos el "from modulo import..." ya no debes indicar el nombre del modulo antes:
		print(areaCirculo(radio))
	elif opcion == 4:
		base = int(input("Dame el base:"))
		altura = int(input("Dame el altura:"))
		#Como importamos modulo as mo mandamos a llamarlo así:
		print(mo.areaRectangulo(base,altura))
	else:
		break