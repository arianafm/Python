# pip3 install requests --user

import requests

parametros = {
	"q" : "perritos"

}

#https = http + TLS: Transfer Layer Security
#get lleva en expuestos los parámetros que le estamos pasando.
#Pasar otro parámetro es opcional pero siempre debe llamarse 'params'
response = requests.get("https://www.google.com", params = parametros)


#Código html de la página...
print(response.text) #Imprime status code <Response [200]> (200 significa éxito, 300 errores de autorización, 400 error de la petición, 500 error del servidor)




#print(dir(response)) Esto te regresaría un json pero el link de google NO nos regresa json