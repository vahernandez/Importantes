"""
Haz un programa que imprima el tiempo que hace en cualquier ciudad del mundo.
Se realizo un archivo .py llamado key, en ese archivo se guardó una variable string osea con comillas, esa variable
es el key que te da la pagina wheatherapi.com despues de registrarse. Este archivo se pone en la misma ubicación que este programa

"""

from key import KEY
import requests
from pprint import pprint

url = "https://api.weatherapi.com/v1/current.json"

ciudad = input("Introduce tu ciudad: ")

respuesta = requests.get(f"https://api.weatherapi.com/v1/current.json?key={KEY}&q={ciudad}")

json = respuesta.json()

#pprint(json)

#print(f"Temperatura en la ciudad de {ciudad}: {json['current']['temp_c']} grados Centigrados")
#print(f"La humedad en la ciudad de {ciudad}: {json['current']['humidity']}")

print(f"La temperatura de la ciudad de {ciudad} es {json['current']['temp_c']} grados centrigrados \n y su humedad es: {json['current']['humidity']} %")


print(f"{json['current']['condition']['text']}")

# voy a guardar la información en un txt:

with open ("C:\inputs\weather.txt", "w") as cache1:
    cache1.write(f"La temperatura de la ciudad de {ciudad} es {json['current']['temp_c']} grados centrigrados \n y su humedad es: {json['current']['humidity']} % \n")
    cache1.write(f"{json['current']['condition']['text']}")

