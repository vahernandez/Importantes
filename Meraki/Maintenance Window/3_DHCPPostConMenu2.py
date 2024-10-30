"""
Este codigo nos configura un dhcp svi, le ponemos un archivo llamado input2.csv y verlo con el DhcpConfigForOneSVI.py
En teoria podemos editar este script una vez que tengamos la información de los ids con el script 2
"""
import requests
import json
import csv

# Diccionario con la información de los sitios
sitios = {
    'a': {'nombre': 'Mexico 510', 'serial': 'Q2LW-45P5-F593', 'interface_id_vlan1': '754915887537981028'},
    'b': {'nombre': 'México 520', 'serial': 'Q2LW-453K-D784', 'interface_id_vlan1': '754915887537980988'},
    'c': {'nombre': 'Columbus', 'serial': 'Q2LW-3CRH-W8F6', 'interface_id_vlan1': '3677189095748010627'},
    'd': {'nombre': 'Appelt', 'serial': 'Q2LW-3D2D-LP5T', 'interface_id_vlan1': '754915887537981876'},
    'e': {'nombre': 'Alsip', 'serial': 'Q2LW-87NE-L45N', 'interface_id_vlan1': '754915887537980857'},
    'f': {'nombre': 'Butler', 'serial': 'Q2LW-8A2B-5GJM', 'interface_id_vlan1': '754915887537980885'},
    'g': {'nombre': 'Birmingham', 'serial': 'Q2LW-9GDX-5G8J', 'interface_id_vlan1': '754915887537980214'},
    'h': {'nombre': 'Post Oak', 'serial': 'Q2LW-89GD-FL29', 'interface_id_vlan1': '754915887537980385'},
    'i': {'nombre': 'Post Oak', 'serial': 'Q2LW-89GD-FL29', 'interface_id_vlan501': '3677189095748011444'} 
}

# Pedir al usuario que seleccione el sitio
print("Seleccione el sitio donde desea aplicar la configuración:")
for key, value in sitios.items():
    print(f"{key}: {value['nombre']}")

sitio_seleccionado = input("Ingrese la letra correspondiente al sitio: ").lower()

# Verificar que la entrada es válida
if sitio_seleccionado not in sitios:
    print("Sitio no válido. Ejecute el script nuevamente y seleccione un sitio válido.")
    exit()

# Obtener los parámetros del sitio seleccionado
serial = sitios[sitio_seleccionado]['serial']
interface_id_vlan1 = sitios[sitio_seleccionado]['interface_id_vlan1']

# Construir la URL con los parámetros del sitio seleccionado
url = f"https://api.meraki.com/api/v1/devices/{serial}/switch/routing/interfaces/{interface_id_vlan1}/dhcp"

# Crear una lista vacía para almacenar las asignaciones de IP fija
fixed_ip_assignments = []

# Leer el archivo CSV con codificación UTF-8
with open(r'C:\RootScripts\Input2.csv', newline='', encoding='utf-8') as csvfile:
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

# Configurar los encabezados de la solicitud
headers = {
    'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa',
    'Content-Type': 'application/json'
}

# Hacer la solicitud PUT a la API
response = requests.request("PUT", url, headers=headers, data=json.dumps(payload))

# Imprimir la respuesta de la API
print(response.text)
