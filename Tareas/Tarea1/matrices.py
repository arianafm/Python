#Elabora un programa que me permita realizar la suma de dos matrices de 3x3. Cada uno de los elementos de la matriz deberá ser ingresado por el usuario. Una matriz en Python puede implementarse con listas dentro de listas.

def elementos():
	#Listas por comprensión
	matriz =[[[] for i in range(3)] for i in range(3)]
	for i in range(3):
		for j in range(3):
			numero = int(input("Ingrese los elementos:")) 
			matriz[i][j] = numero
	return matriz

#print(*x): Desempaca la lista dentro de la llamada de impresión.
def imprime(matriz):
	for x in matriz:
		print(*x)

def suma(ma1,ma2):
	result = [[0,0,0], [0,0,0], [0,0,0]] 
	for i in range(len(ma1)):    
	    for j in range(len(ma1[0])): 
	        result[i][j] = ma1[i][j] + ma2[i][j] 
	return result

print("___SUMA DE MATRICES___\n")

print("Primer matriz:")
matriz1 = elementos()
#print(matriz1)
imprime(matriz1)
print("\n")

print("Segunda matriz:")
matriz2 = elementos()
#print(matriz2)
imprime(matriz2)
print("\n")

matrizfin = suma(matriz1,matriz2)
print("Matriz resultante:")
imprime(matrizfin)

