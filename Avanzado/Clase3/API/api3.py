# pip3 install requests --user

import requests

parametros = {
	"q" : "perritos"

}

#api publica para ejemplificar...
#Información generada al azar de una persona. (Información falsa para llenar base de datos,etc...)
"""
for i in range(50):
	response = requests.get("https://randomuser.me/api/")
	persona = response.json()
	print(persona)
"""

#requests.post()
#console.cloud.google.com
#developers.google.com

response = requests.get("https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=AIzaSyD4X1l76Tkn5O3OdrGaUQNlnizjgrxCTvM")

print(response.status_code)
print(response.json())

"""
Si todo salio bien imprime la dirección predeterminada.
EstadosUnidos39:Desktop cur01alu39$ python3 api3.py
200
{'results': [{'address_components': [{'long_name': '1600', 'short_name': '1600', 'types': ['street_number']}, {'long_name': 'Amphitheatre Parkway', 'short_name': 'Amphitheatre Pkwy', 'types': ['route']}, {'long_name': 'Mountain View', 'short_name': 'Mountain View', 'types': ['locality', 'political']}, {'long_name': 'Santa Clara County', 'short_name': 'Santa Clara County', 'types': ['administrative_area_level_2', 'political']}, {'long_name': 'California', 'short_name': 'CA', 'types': ['administrative_area_level_1', 'political']}, {'long_name': 'United States', 'short_name': 'US', 'types': ['country', 'political']}, {'long_name': '94043', 'short_name': '94043', 'types': ['postal_code']}], 'formatted_address': '1600 Amphitheatre Pkwy, Mountain View, CA 94043, USA', 'geometry': {'location': {'lat': 37.4224095, 'lng': -122.0856043}, 'location_type': 'ROOFTOP', 'viewport': {'northeast': {'lat': 37.4237584802915, 'lng': -122.0842553197085}, 'southwest': {'lat': 37.4210605197085, 'lng': -122.0869532802915}}}, 'place_id': 'ChIJtYuu0V25j4ARwu5e4wwRYgE', 'plus_code': {'compound_code': 'CWC7+XQ Mountain View, California, United States', 'global_code': '849VCWC7+XQ'}, 'types': ['street_address']}], 'status': 'OK'}
"""