#pip3 install requests --user

import requests
import pprint

API_TOKEN = "AIzaSyD4X1l76Tkn5O3OdrGaUQNlnizjgrxCTvM"
GEOCODING_URL = "https://maps.googleapis.com/maps/api/geocode/json"


direccion = input("¿Qué lugar buscas?") #Six flags Mexico
parametros = {

	"key": API_TOKEN,
	"address": direccion
	
}


response = requests.get(GEOCODING_URL, params=parametros)
pprint.pprint(response.json(), indent=4)

"""
IMPRIME:
EstadosUnidos39:Desktop cur01alu39$ python3 api.py
¿Qué lugar buscas?Six flags Mexico
{   'results': [   {   'address_components': [   {   'long_name': 'Km 1.5',
                                                     'short_name': 'Km 1.5',
                                                     'types': [   'street_number']},
                                                 {   'long_name': 'Carr. '
                                                                  'Picacho-Ajusco',
                                                     'short_name': 'Carr. '
                                                                   'Picacho-Ajusco',
                                                     'types': ['route']},
                                                 {   'long_name': 'Tlalpan',
                                                     'short_name': 'Tlalpan',
                                                     'types': [   'political',
                                                                  'sublocality',
                                                                  'sublocality_level_1']},
                                                 {   'long_name': 'Ciudad de '
                                                                  'México',
                                                     'short_name': 'México '
                                                                   'D.F.',
                                                     'types': [   'locality',
                                                                  'political']},
                                                 {   'long_name': 'Ciudad de '
                                                                  'México',
                                                     'short_name': 'CDMX',
                                                     'types': [   'administrative_area_level_1',
                                                                  'political']},
                                                 {   'long_name': 'Mexico',
                                                     'short_name': 'MX',
                                                     'types': [   'country',
                                                                  'political']},
                                                 {   'long_name': '14200',
                                                     'short_name': '14200',
                                                     'types': ['postal_code']}],
                       'formatted_address': 'Carr. Picacho-Ajusco Km 1.5, '
                                            'Tlalpan, 14200 Ciudad de México, '
                                            'CDMX, Mexico',
                       'geometry': {   'location': {   'lat': 19.2956057,
                                                       'lng': -99.21056519999999},
                                       'location_type': 'ROOFTOP',
                                       'viewport': {   'northeast': {   'lat': 19.2969546802915,
                                                                        'lng': -99.20921621970848},
                                                       'southwest': {   'lat': 19.2942567197085,
                                                                        'lng': -99.2119141802915}}},
                       'place_id': 'ChIJGZTVlcn_zYURRZxrmu06Qto',
                       'plus_code': {   'compound_code': '7QWQ+6Q Mexico City, '
                                                         'Mexico',
                                        'global_code': '76F27QWQ+6Q'},
                       'types': [   'amusement_park',
                                    'establishment',
                                    'point_of_interest']}],
    'status': 'OK'}
EstadosUnidos39:Desktop cur01alu39$ 


"""