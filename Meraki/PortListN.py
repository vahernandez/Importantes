import requests
import json
import csv

url = "https://api.meraki.com/api/v1/devices/Q4CA-SPCX-FVTX/switch/ports"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    json_data = response.json()
    
    # Seleccionar las columnas necesarias para el CSV
    selected_columns = ['portId', 'name', 'type', 'vlan', 'voiceVlan', 'allowedVlans', 'rstpEnabled']
    
    # Guardar la respuesta en un archivo CSV
    output_file = "C:\RootScripts\LstPtsN.csv"
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=selected_columns)
        writer.writeheader()
        for port in json_data:
            writer.writerow({key: port.get(key, '') for key in selected_columns})
    
    print("El output ha sido guardado en el archivo 'output.csv'.")
else:
    print("Error: No se pudo obtener la respuesta del servidor.")
