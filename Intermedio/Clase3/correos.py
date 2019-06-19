import smtplib
import getpass 

#tls le agrega una capa más de seguridad.
def enviar_correo(remitente, passsword, destinatario, asunto, cuerpo):
	print("Preparando el correo...")
	#Se pone el servidor de correo.
	#587 es el puerto que utiliza gmail.
	#smtp es el protocolo.
	smtpserver = smtplib.SMTP("smtp.gmail.com",587)

	# PAsos del protocolo SMTP
	smtpserver.ehlo() # Saludo al servidor
	smtpserver.starttls() # Agrega otra capa de seguridad
	try:
		smtpserver.login(remitente, passsword)
	except:
		print("NO has configurado tu correo, favor de revisar.")

	#Se usan expresiones regulares para asegurarse de que el header este bien escrito.
	#header son cabeceras que llevan metadatos, los datos se comparten con json y el header 
	#la llave del diccionario.
	#Los header llevan el from y el subject en este caso.
	header = "To: {0}\nFrom: {1}\nSubject: {2}\n".format(destinatario,remitente,asunto)
	msg = header + "\n{0}\n\n".format(cuerpo)
	print(msg)

	smtpserver.sendmail(remitente,destinatario,msg)
	#Cierra flujos.
	#Si no lo cerramos pueden quedar procesos abiertos que consumen la RAM.
	smtpserver.close()

if __name__ == "__main__":

	usuario = input("Escriba el remitente:")
	passsword = getpass.getpass("Escriba su contraseña:")
	destinario = input("Escriba el destinario:")
	asunto = input("Escriba el asunto:")
	cuerpo = input("Escriba su mensaje:")ç
	#El for es para hacer spam.
	for x in range(1,4):
		enviar_correo(usuario,passsword,destinario,asunto,cuerpo)