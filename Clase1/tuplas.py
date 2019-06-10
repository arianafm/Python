# T U P L A S
x = ("a", "b", "c")
print(x[1])

#Transformar tupla a lista
y = list(x)
print(type(y))

#Transformar lista a tupla:
w = [1,2,4,5]
c = tuple(w)
print(type(c))
print(c)

#Probemos que las tuplas NO pueden modificar su valor...

# print(c[2])
# c[2] = "Hola"
'''
Traceback (most recent call last):
  File "tuplas.py", line 17, in <module>
    c[2] = "Hola"
TypeError: 'tuple' object does not support item assignment
'''

                                                                                                                  
