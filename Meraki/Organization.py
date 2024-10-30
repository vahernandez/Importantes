import requests
import json

url = "https://api.meraki.com/api/v1/organizations/848368/networks"
payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

"""
# Convertir la respuesta a formato JSON con indentación para una mejor legibilidad
formatted_response = json.dumps(response.json(), indent=2)

print(formatted_response)

""" 


##################################################################################

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a JSON
    networks = response.json()
    
    # Iterar sobre cada red y mostrar el nombre
    for network in networks:
        print(network["name"])
else:
    print("Error:", response.status_code)

