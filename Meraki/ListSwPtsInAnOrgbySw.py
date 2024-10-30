import requests
import csv
import json

url = "https://api.meraki.com/api/v1/organizations/848368/switch/ports/bySwitch"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Convertir la respuesta a formato JSON
data = response.json()

# Filtrar los resultados solo para la red "Mexico520"
filtered_data = [item for item in data if item.get("network", {}).get("name") == "Mexico520"]

# Guardar los datos filtrados en un archivo CSV
with open("C:\RootScripts\SwPts.csv", "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=filtered_data[0].keys())
    writer.writeheader()
    writer.writerows(filtered_data)

# Imprimir los datos filtrados en formato JSON
print(json.dumps(filtered_data, indent=4))