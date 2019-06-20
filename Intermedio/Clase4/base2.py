# -*- coding: utf-8 -*-

import sqlite3

#Misma base de datos que en base1.py
conexion = sqlite3.connect("ejemplo.db")
cursor = conexion.cursor()

alumnos = [('Ariana',18,316087698,10),('Hannah',19,316087699,10)]
#Le puedes pasar toda tu lista de tuplas y lo hará.
#Los signos de ? funcionarám como comodines.
cursor.executemany("INSERT INTO alumno VALUES(?,?,?,?)",alumnos)
cursor.execute("SELECT * FROM alumno")
alumnitos = cursor.fetchall()
print(alumnitos)
#Cambiando el nombre de la tabla:

#renombrar = "ALTER TABLE alumno RENAME TO student"
#cursor.execute(renombrar)

conexion.commit()
conexion.close()