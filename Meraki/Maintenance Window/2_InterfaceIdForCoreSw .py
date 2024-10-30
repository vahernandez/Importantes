"""
import requests
import json
import csv

url = "https://api.meraki.com/api/v1/devices/Q2LW-453K-D784/switch/routing/interfaces"

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
    output_file = "C:/RootScripts/SVIsId.csv"
    with open(output_file, "w", newline="") as csvfile:
        # Escribir los datos JSON en el archivo CSV
        writer = csv.DictWriter(csvfile, fieldnames=json_data[0].keys())
        writer.writeheader()
        writer.writerows(json_data)
    
    print("El output ha sido guardado en el archivo 'output.csv'.")
    print(json_data)
else:
    print("Error: No se pudo obtener la respuesta del servidor.")
"""
# vamos a obtener los ids de las svi que nos sirven para configurar el dhcp statico
import requests
import json
import csv

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
    
    # Obtener todos los campos presentes en los datos JSON
    all_fields = set()
    for interface in json_data:
        all_fields.update(interface.keys())
    
    # Guardar la respuesta en un archivo CSV
    output_file = "C:/RootScripts\PostOak/SVIsId.txt"
    with open(output_file, "w", newline="") as csvfile:
        # Escribir los datos JSON en el archivo CSV
        writer = csv.DictWriter(csvfile, fieldnames=all_fields)
        writer.writeheader()
        writer.writerows(json_data)
    
    print("El output ha sido guardado en el archivo 'SVIsId.txt'.")
else:
    print("Error: No se pudo obtener la respuesta del servidor.")


# Este script te da en un archivo txt llamado SVIsID la lista de los InterfaceId por sitio, esta id es necesario para usar el script DhcpConfig