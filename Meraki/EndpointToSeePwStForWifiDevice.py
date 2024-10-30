import requests
import json
import csv

url = "https://api.meraki.com/api/v1/organizations/848368/wireless/devices/ethernet/statuses"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    json_data = response.json()
    
    # Guardar la respuesta en un archivo CSV
    output_file = "C:/RootScripts/endpoint.csv"
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        # Escribir encabezados
        writer.writerow(json_data[0].keys())
        # Escribir datos
        for device in json_data:
            writer.writerow(device.values())
    
    print("El output ha sido guardado en el archivo 'output.csv'.")
else:
    print("Error: No se pudo obtener la respuesta del servidor.")
    
