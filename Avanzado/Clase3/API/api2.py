# pip3 install requests --user

import requests

parametros = {
	"q" : "perritos"

}

#api publica para ejemplificar...
#Información generada al azar de una persona. (Información falsa para llenar base de datos,etc...)
response = requests.get("https://randomuser.me/api/")
persona = response.json()
for i in persona:
	print(i,persona[i])


print(response.text)