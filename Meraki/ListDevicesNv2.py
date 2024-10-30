import requests
import json
import csv

url ="https://api.meraki.com/api/v1/networks/L_754915887537980170/devices"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Convert the response to JSON format
data = response.json()


# Seleccionar solo las columnas necesarias
selected_columns = ['serial', 'mac', 'lanIp', 'networkId', 'name', 'model']

# Filtrar los dispositivos que tienen una dirección IP asignada
#filtered_data = [{key: device[key] for key in selected_columns} for device in data if device.get('lanIp')]

# Filtrar los dispositivos que tienen una dirección IP asignada y que son switches
filtered_data = [{key: device[key] for key in selected_columns} for device in data if device.get('lanIp') and device.get('model', '').startswith('MS')]


"""
# Guardar la salida en un archivo CSV
output_file = "C:/RootScripts/listDevicesN.csv"  # Ruta del archivo de salida
with open(output_file, "w", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=selected_columns)
    writer.writeheader()
    writer.writerows(filtered_data)

print("Salida guardada en listDevicesN.csv")
"""


# Guardar la salida en un archivo CSV con pestañas separadas
output_file_prefix = "C:/RootScripts/device23sept3"  # Prefijo para el nombre del archivo
for i, device in enumerate(filtered_data, start=1):
    output_file = output_file_prefix + str(i) + ".csv"  # Nombre del archivo para cada dispositivo
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=selected_columns)
        writer.writeheader()
        writer.writerow(device)

print("Salidas guardadas en archivos CSV con pestañas separadas.")

