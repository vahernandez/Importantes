import requests
from pprint import pprint

url = "https://pokeapi.co/api/v2/pokemon/"  # un sitio que puedas hacer llamadas 

resp = requests.get(url)

respjson = resp.json()


# si quiero solo las llaves del diccionario:



print("***************************************************************")
# Si quiero algún valor de uno de las llaves por ejemplo "next":




print("***************************************************************")

# Si quiero todos los valores de las llaves:




print("***************************************************************")

#Quiero la url de charmeleon:





print("***************************************************************")

#Quiero todos los nombres de los pokemons:
