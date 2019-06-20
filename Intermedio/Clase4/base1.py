# -*- coding: utf-8 -*-
#Lo de arrriba es para hacer comentarios con utf8
import sqlite3

#A todas las bases de datos les vamos a pasar un archivo de tipo db(data base)
conexion = sqlite3.connect("ejemplo.db")
#Dentro de SQL existe una extension que se llama cursor y este nos permite ejecutar las acciones.
#Cursor te ayuda a recorrer todas las filas de tu tabla.
cursor = conexion.cursor()
#Instrucción y el nombre de la tabla.
#SQL.
#Atributos.
#varchar es el equivalente a una cadena en Python.
try:
	#Creación de la tabla.
	#Marca error cuando la tabla ya está creada.
	cursor.execute("CREATE TABLE alumno(nombre varchar(30), edad integer, num_cuenta integer, calificacion integer CHECK(calificacion>0 and calificacion<=10))")

#Except todas las excepciones que puede haber
#except:
#Ponemos el error desde sqlite3 pues este error NO es propio de python.
except sqlite3.OperationalError:
	print("Ha ocurrido un error.")

finally:
	cursor.execute("INSERT INTO alumno VALUES('Hannah',20,123456,10)")
	cursor.execute("INSERT INTO alumno VALUES('Rodrigo',23,67895,10)")
	cursor.execute("INSERT INTO alumno VALUES('Aldo',24,743256,10)")
	cursor.execute("INSERT INTO alumno VALUES('Malaika',22,0980706,10)")
	cursor.execute("INSERT INTO alumno VALUES('Ariana',18,316087698,10)")

#Recuperando contenido de las tablas:
cursor.execute("SELECT * FROM alumno")

#Creando variable llamada alumno al cual le pasaremos el cursor:
alumno = cursor.fetchone()
print(alumno)
#Trae otras tres coincidencias.
alumnos = cursor.fetchmany(3)
print(alumnos)
conexion.commit()
conexion.close()