import requests
import csv
import json

url = "https://api.meraki.com/api/v1/networks/L_754915887537980170/devices"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

# Realiza la solicitud GET
response = requests.request("GET", url, headers=headers, data=payload)

# Convierte la respuesta en JSON
devices = response.json()

# Definir el nombre del archivo CSV
csv_file = "C:/RootScripts/InventoryWithFirmware.csv"

# Crear un conjunto para todas las llaves posibles
all_keys = set()

# Encontrar todas las posibles llaves en los dispositivos
for device in devices:
    all_keys.update(device.keys())

# Convertir el conjunto de llaves a una lista ordenada (opcional)
keys = list(all_keys)

# Guardar la respuesta en un archivo CSV
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=keys)
    
    # Escribir las cabeceras
    writer.writeheader()
    
    # Escribir los datos de cada dispositivo
    for device in devices:
        # Escribir solo los campos que existen en el dispositivo actual
        writer.writerow({key: device.get(key, '') for key in keys})

print(f"Data saved to {csv_file}")
