import sqlite3
conexion = sqlite3.connect("banco.db")
cursor = conexion.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS cliente(cliente_id integer PRIMARY KEY AUTOINCREMENT, nombre varchar(30), edad integer, curp varchar(18))")
cursor.execute("CREATE TABLE IF NOT EXISTS tarjeta(tarjeta_id integer PRIMARY KEY AUTOINCREMENT, numero varchar(16) UNIQUE, clave varchar(4), fecha_vencimiento DATE, cliente_id INTEGER references cliente(cliente_id))")

bandera = True
while bandera:
	try:
		print("Selecciona una opción")
		print("\t1.-Insertar un cliente")
		print("\t2.-Insertar una tarjeta")
		print("\t3.-Consultar un cliente")
		print("\t4.-Actualizar un cliente")
		print("\t5.-Borrar un cliente")
		print("\t6.-Salir")
		opcion = int(input("\t=>"))
		if opcion == 1:
			nombre = input("Dame tu nombre: ")
			edad = int(input("Dame tu edad: "))
			curp = input("Dame el curp:")
			cursor.execute("INSERT INTO cliente(nombre, edad, curp) VALUES ('%s', '%d', '%s')"%(nombre, edad, curp))
			print("Dato insertado en la tabla.")
			conexion.commit()

		elif opcion == 2:
			numero = input("Dame tu número de tu tarjeta: ")
			clave = input("Dame la clave: ")
			fecha = input("Dame la fecha de vencimiento en el formato: yyyy/mm/dd")
			cliente = input("Dame el nombre del cliente: ")
			cursor.execute("SELECT cliente_id from cliente where nombre='%s')"%(cliente))
			num_cliente = cursor.fetchone()
			cursor.execute("INSERT INTO tarjeta(numero, clave, fecha_vencimiento, cliente_id) VALUES ('%s', '%s', DATE(%s, 'YYY/MM/DD'), '%s')"%(numero, clave, fecha_vencimiento, cliente_id[0]))
			print("Dato insertado correctamente.")
			conexion.commit()

		elif opcion == 3:
			pass

		elif opcion == 4:
			nombre = input("Dame el nombre del cliente a actualizar:")
			edad = int(input("Dame la nueva edad:"))
			curp = input("Dame el nuevo CURP")
			cursor.execute("UPDATE cliente SET edad =%d where nombre = '%s'"%(edad,nombre))
			cursor.execute("UPDATE cliente SET curp =%d where nombre = '%s'"%curp,nombre)
			print("Dato actualizado correctamente.")
			conexion.commit()
		elif opcion == 5:
			nombre = input("Dame el cliente a borrar: ")
			#¡¡¡¡¡¡¡¡¡¡RECUERDA QUE EL DELETE SIEMPRE LLEVA UN WHERE!!!!!!!!!
			cursor.execute("DELETE FROM cliente where nombre = '%s'"%(nombre))
			print("Cliente eliminado correctamente")
			conexion.commit()
		elif opcion == 6:
			print("Adiós.")
			bandera = False

	except Exception:
		print("ERROR EN LA EJECUCIÓN.")

conexion.commit()
conexion.close()


















