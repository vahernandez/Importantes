# Llamada de API en pyhon

from pprint import pprint
import requests

url = "https://pokeapi.co/api/v2/pokemon/"  # un sitio que puedas hacer llamadas 

respuesta = requests.get(url)

respJson = respuesta.json()

#pprint (respJson)

charizard_url = ''
for i in respJson['results']: # Por cada elemento del diccionario de la sección 'results'
    if i['name'] == 'charizard':   # busca en la sección de ´name' el string de charizard
        charizard_url = i['url']   # y solo en ese caso cuando hayas encontrado el string url, guardalo en la variable
        
#print(charizard_url)

respCharizard_url = requests.get(charizard_url)
respCharizardJson = respCharizard_url.json()

#pprint(respCharizardJson)

with open('C:\\inputs\\pokemon.txt', 'w') as cache3:
    cache3.write(str(respCharizardJson))



