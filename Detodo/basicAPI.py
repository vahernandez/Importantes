# Llamada de API en pyhon
from pprint import pprint
import requests

url = "https://pokeapi.co/api/v2/pokemon/"  # un sitio que puedas hacer llamadas 

respuesta = requests.request("GET", url)  # las dos formas dan el mismo resultado pero esta forma puede agregar header osea la authen y payload
respuestas= requests.get (url)   # usamos el metodo get de REST


pprint(respuesta.json())  # lo queremos en formato json
pprint(respuestas.json()) # y que se vea vertical y ordenado con pprint

