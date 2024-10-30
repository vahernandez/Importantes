import requests
from pprint import pprint

url = "https://pokeapi.co/api/v2/pokemon/"  # un sitio que puedas hacer llamadas 

pokemon = requests.get(url)

print (pokemon)

pokemonJson = pokemon.json()


charizard = ''


for i in pokemonJson['results']:
    if i['name'] == 'charizard':
        print(i['url'])