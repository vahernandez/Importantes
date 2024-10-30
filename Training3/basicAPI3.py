import requests
from pprint import pprint

url = "https://pokeapi.co/api/v2/pokemon/"  # un sitio que puedas hacer llamadas 

resp = requests.get(url)

respjson = resp.json()


# si quiero solo las llaves del diccionario:
for i in respjson:
    print(i)

print("***************************************************************")
# Si quiero algún valor de uno de las llaves por ejemplo "next":
next = respjson['next']
print(next)

print("***************************************************************")

# Si quiero todos los valores de las llaves:

for i in respjson.values():
    pprint(i)

print("***************************************************************")

#Quiero la url de charmeleon:

for j in respjson['results']:
    if j['name']== 'charmeleon':
        print(j['url'])


print("***************************************************************")

#Quiero todos los nombres de los pokemons:
for i in respjson['results']:
    print(i['name'] )