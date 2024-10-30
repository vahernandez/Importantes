import requests
from pprint import pprint

url = "https://pokeapi.co/api/v2/pokemon/"  # un sitio que puedas hacer llamadas 

resp = requests.get(url)

respJson = resp.json()

#pprint(respJson)

for i in respJson:
    print(i)
    if i == 'results':
        results = respJson['results'] 
        for j in results:
            print(j)
            if j['name']== 'wartortle':
                print(j['url'])
        
                
                
                
"""
if 'results' in respJson:
    results = respJson['results']
    for j in results:
        if j['name'] == 'wartortle':
            print(j['url'])
else:
    print("La respuesta no contiene la clave 'results'")
"""       
