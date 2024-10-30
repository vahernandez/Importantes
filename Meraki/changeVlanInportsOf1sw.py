"""
import requests
import json

url = "https://api.meraki.com/api/v1/devices/Q2KW-4CY8-6FLC/switch/ports/24"

payload = json.dumps({
  "name": "null",
  "enabled": True,
  "poeEnabled": True,
  "type": "access",
  "vlan": 21,
  "rstpEnabled": True,
  "stpGuard": "loop guard"
})
headers = {
  'Content-Type': 'application/json',
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("PUT", url, headers=headers, data=payload)

print(response.text)

"""

import csv
import requests
import json

# Función para enviar la solicitud PUT
def enviar_solicitud(url, payload, headers):
    response = requests.put(url, headers=headers, data=json.dumps(payload))
    print(response.text)

# URL base
base_url = "https://api.meraki.com/api/v1/devices/Q2KW-4CY8-6FLC/switch/ports/"

# Cabeceras
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

# Leer el archivo CSV
with open('C:/RootScripts/datos.csv', mode='r') as file:
    datos_csv = csv.reader(file)
    next(datos_csv)  # Saltar la primera fila (cabecera)
    for row in datos_csv:
        puerto_id = row[0]  # ID del puerto
        vlan = int(row[1])  # VLAN

        # Construir la URL completa con el ID del puerto
        url = base_url + f"{puerto_id}"

        # Payload con la nueva VLAN
        payload = {
            "enabled": True,
            "poeEnabled": True,
            "type": "access",
            "rstpEnabled": True
        }

        # Enviar la solicitud PUT
        enviar_solicitud(url, payload, headers)
