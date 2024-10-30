# Llamada de API en pyhon

from pprint import pprint
import requests
import json

url = "https://pokeapi.co/api/v2/pokemon/"  # un sitio que puedas hacer llamadas 

respuesta = requests.get(url)

respJson = respuesta.json()

#pprint (respJson)

charizard_url = ''

for i in respJson['results']:
    if i['name'] == 'charizard':
        print(i['url'])
        charizard_url = i['url']

respCharizard = requests.get(charizard_url)

respCharJson = respCharizard.json()

# Formatea los datos para una mejor legibilidad
formatted_data = json.dumps(respCharJson, indent=4)

#with open('C:\\inputs\\pokemon2.txt', 'w') as cache1:
    #cache1.write(str(formatted_data))

#pprint(respCharJson)
for i in respCharJson["abilities"]:
    for j in i["ability"]:
        if i["ability"]["name"] == 'blaze':
            print(i["ability"]['url'])
    
    

"""
    for j in i["ability"]:
        if j["name"]=="blaze":
            print(j["url"])
"""    

    

