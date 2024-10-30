"""
Este codigo nos configura un dhcp svi, le ponemos un archivo llamado input2.csv y verlo con el DhcpConfigForOneSVI.py
"""
import requests
import json
import csv

url = "https://api.meraki.com/api/v1/devices/Q2LW-9GDX-5G8J/switch/routing/interfaces/3677189095748011574/dhcp"           #<<<<<<<<<<<<<<<< Cambiar el serial del switch core y el Id con el Script 2 

# Crear una lista vacía para almacenar las asignaciones de IP fija
fixed_ip_assignments = []

# Leer el archivo CSV
# Leer el archivo CSV con codificación UTF-8
with open(r'C:\RootScripts\Input2old2.csv', newline='', encoding='utf-8') as csvfile:                                    #<<<<<<<<<<<<<<<<<<<<<< Cambiar path
    reader = csv.DictReader(csvfile)
    

    # Iterar sobre cada fila del archivo CSV
    for row in reader:
        # Construir un diccionario para cada fila y agregarlo a la lista de asignaciones de IP fija
        assignment = {
            "name": row["name"],
            "mac": row["mac"],
            "ip": row["ip"]
        }
        fixed_ip_assignments.append(assignment)

# Construir el payload con las asignaciones de IP fija
payload = {
    "fixedIpAssignments": fixed_ip_assignments
}

headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa',
  'Content-Type': 'application/json'
}

response = requests.request("PUT", url, headers=headers, data=json.dumps(payload))

print(response.text)
