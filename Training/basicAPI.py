# Llamada de API en pyhon
from pprint import pprint
import requests

url = "https://pokeapi.co/api/v2/pokemon/"  # un sitio que puedas hacer llamadas 

respuesta = requests.get(url)

# Convertir la respuesta a json

data = respuesta.json()

# Encontrar la url de charizard en los resultados:

charizard_url = ''

for pokemon in data['results']:
    if pokemon['name'] == 'charizard':
        charizard_url = pokemon['url']
        break
print("Esta es la url de charizard \n ", charizard_url)    

if charizard_url != None:
    charizard_respuesta = requests.get(charizard_url)
    charizard_data = charizard_respuesta.json()
    pprint(charizard_respuesta)
else:
    pass