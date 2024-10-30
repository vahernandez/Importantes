# Llamada de API en pyhon

from pprint import pprint
import requests

url = "https://pokeapi.co/api/v2/pokemon/"  # un sitio que puedas hacer llamadas 

respuesta = requests.get(url)

# Convertir la respuesta a json:

respJson = respuesta.json()
# esto es lo que se ve si hacemos un print de respJson:
"""
<Response [200]>
{'count': 1302,
 'next': 'https://pokeapi.co/api/v2/pokemon/?offset=20&limit=20',
 'previous': None,
 'results': [{'name': 'bulbasaur',
              'url': 'https://pokeapi.co/api/v2/pokemon/1/'},
             {'name': 'ivysaur', 'url': 'https://pokeapi.co/api/v2/pokemon/2/'},
             {'name': 'venusaur',
              'url': 'https://pokeapi.co/api/v2/pokemon/3/'},
             {'name': 'charmander',
              'url': 'https://pokeapi.co/api/v2/pokemon/4/'},
             {'name': 'charmeleon',
              'url': 'https://pokeapi.co/api/v2/pokemon/5/'},
             {'name': 'charizard',
              'url': 'https://pokeapi.co/api/v2/pokemon/6/'},
"""

# Encontrar la url de charizard en los resultados.


charizard_url = ''

for i in respJson['results']:  # Queremos encontrar dentro de results a el string charizard (valor)
    if i['name'] == 'charizard': # se intera sobre todos los valores de result
        charizard_url = i['url']  # una vez que se encuentre el diccionario dentro de la lista result se 
        break    # se guarda en una nueva variable

# en este punto ya tenemos la url de charizard guardada en una variable
# esta nueva url tiene información nueva.

if charizard_url != None: 
    charizard_respuesta = requests.get(charizard_url)  # le hacemos get a esta nueva url
    charizard_resJson = charizard_respuesta.json()   # convertimos a json
    pprint(charizard_resJson)
#pprint(respJson)