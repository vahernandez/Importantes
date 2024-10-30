"""
import requests

url = "https://api.meraki.com/api/v1/devices/Q2KW-4CY8-6FLC/switch/ports"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

"""

import requests
import csv
from datetime import datetime

url = "https://api.meraki.com/api/v1/devices/Q2KW-4CY8-6FLC/switch/ports"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Obtener la fecha y hora actual
now = datetime.now()
timestamp = now.strftime("%Y-%m-%d_%H-%M-%S")

# Nombre del archivo CSV
csv_file_name = f"C:\\RootScripts\\puertos_{timestamp}.csv"

#f"puertos_{timestamp}.csv"

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta JSON a un diccionario
    data = response.json()
    
    # Guardar la respuesta en un archivo CSV
    with open(csv_file_name, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        
        # Escribir los encabezados
        writer.writerow(data[0].keys())
        
        # Escribir los datos
        for port in data:
            writer.writerow(port.values())
    
    print(f"La respuesta ha sido guardada en el archivo '{csv_file_name}'.")
else:
    print("Error: No se pudo obtener la respuesta del servidor.")
