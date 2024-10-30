"""import requests

url = "https://api.meraki.com/api/v1/devices/Q4CA-SPCX-FVTX/switch/ports/statuses"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

"""

import requests
import json

url = "https://api.meraki.com/api/v1/devices/Q4CA-SPCX-FVTX/switch/ports/statuses"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    json_data = response.json()
    
    # Guardar la respuesta en un archivo de texto en formato JSON
    with open("C:\RootScripts\statusPort.csv", "w") as file:
        json.dump(json_data, file, indent=4)
    
    print("El output ha sido guardado en el archivo 'output.json'.")
else:
    print("Error: No se pudo obtener la respuesta del servidor.")