#Sucesión de Fibonacci:
# 1 1 2 3 5 8 13

def fibo(num):
	if num == 0:
		return 0
	elif num == 1 or num == 2:
		return 1
	else:
		return fibo(num-1)+fibo(num-2)

print(fibo(3))