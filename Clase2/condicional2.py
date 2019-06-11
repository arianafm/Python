#Evaluar comparaciones

import random

x = random.randint(1,101)

#Uso del if
"""
if x<50:
	print("El número es {0} y es menor a 50.".format(x))
else:
	print("El número es {0} y es mayor a 50.".format(x))
"""

#Uso de else if
if x < 10:
	print("El número es {0} y es menor a 10.".format(x))

elif x > 10 and x < 20:
	print("El número es {0} y mayor a 10 y menor a 20.".format(x))

elif x > 20 and x < 30:
	print("El número es {0} y mayor a 20 y menor a 30.".format(x))

else:
	print("El número es {0} y es mayor a 30.".format(x))