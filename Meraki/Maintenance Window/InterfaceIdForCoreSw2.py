import requests
import csv
from datetime import datetime

url = "https://api.meraki.com/api/v1/devices/Q2LW-89GD-FL29/switch/routing/interfaces"

payload = {}
headers = {
    'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    json_data = response.json()
    
    # Filtrar los campos específicos que deseas
    filtered_data = []
    fields_to_keep = ['name', 'interfaceIp', 'defaultGateway', 'vlanId', 'interfaceId', 'subnet']
    
    for interface in json_data:
        filtered_interface = {key: interface.get(key, '') for key in fields_to_keep}
        filtered_data.append(filtered_interface)
    
    # Obtener la fecha y hora actuales
    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    
    # Crear el nombre del archivo con fecha y hora
    output_file = f"C:/RootScripts/PostOak/SVIsId_{timestamp}.txt"
    
    # Guardar la respuesta filtrada en un archivo CSV
    with open(output_file, "w", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fields_to_keep)
        writer.writeheader()
        writer.writerows(filtered_data)
    
    print(f"El output filtrado ha sido guardado en el archivo '{output_file}'.")
else:
    print("Error: No se pudo obtener la respuesta del servidor.")
