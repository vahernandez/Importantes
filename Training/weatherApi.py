"""
Api weather
"""
from pprint import pprint
import requests
from key import KEY
url = "https://api.weatherapi.com/v1/current.json"
ciudad = input(" Que ciudad quieres saber la temperatura ? \n")
respuesta = requests.get(f"https://api.weatherapi.com/v1/current.json?key={KEY}&q={ciudad}")
data = respuesta.json()

#pprint(data)

# Segunda llamada

url_humidity = ''

for i in data['current']:
    if i =='humidity':
        url_humidity = data['current']['humidity']
        print(url_humidity)
        