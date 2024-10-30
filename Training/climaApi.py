"""
Consulta la temperatura actual de una ciudad cualquiera
"""
import requests
ciudad = input("¿De que ciudad quieres saber el tiempo actual? \n")

url = "http://wttr.in/" + ciudad + "?format=3" 
respuesta = requests.get(url)
data = respuesta.text

print(f'Las condiciones climatológicas actuales de la ciudad de {data}')