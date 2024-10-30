import requests
import csv
import json

url = "https://api.meraki.com/api/v1/organizations/848368/switch/ports/bySwitch?"

network_ids = ["L_609674799555296477"]  # Coloca el ID de red dentro de un array

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Convertir la respuesta a formato JSON
data = response.json()

# Guardar los datos en un archivo CSV
with open("C:\RootScripts\SwPts4.csv", "w", newline="") as csvfile:
    fieldnames = data[0].keys()
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

# Guardar los datos en un archivo JSON
#with open("output.json", "w") as jsonfile:
#    json.dump(data, jsonfile, indent=4)

print("Los datos se han guardado en output.csv y output.json")