"""
Este codigo nos configura un dhcp svi, le ponemos un archivo llamado input2.csv y verlo con el DhcpConfigForOneSVI.py
En teoria podemos editar este script una vez que tengamos la información de los ids con el script 2

import requests
import json
import csv

# Diccionario con la información de los sitios
sitios = {
	'a': {'nombre': 'LabIT3', 'serial': 'Q2LW-45P5-F593', 'interface_id_Printers': '3677189095748011490'}, 
	'b': {'nombre': 'LabIT3', 'serial': 'Q2LW-45P5-F593', 'interface_id_Contractors': '3677189095748011492'}, 
	'c': {'nombre': 'LabIT3', 'serial': 'Q2LW-45P5-F593', 'interface_id_Spare Vlan': '3677189095748011494'}, 
	'd': {'nombre': 'LabIT3', 'serial': 'Q2LW-45P5-F593', 'interface_id_Unused ports': '3677189095748011495'}, 
	'e': {'nombre': 'LabIT3', 'serial': 'Q2LW-45P5-F593', 'interface_id_NPS Guest': '3677189095748011491'}, 
	'f': {'nombre': 'LabIT3', 'serial': 'Q2LW-45P5-F593', 'interface_id_Cabling': '3677189095748011487'}, 
	'g': {'nombre': 'LabIT3', 'serial': 'Q2LW-45P5-F593', 'interface_id_NPS Warehouse': '3677189095748011488'}, 
	'h': {'nombre': 'LabIT3', 'serial': 'Q2LW-45P5-F593', 'interface_id_NPSIot': '3677189095748011489'}, 
	'i': {'nombre': 'LabIT3', 'serial': 'Q2LW-45P5-F593', 'interface_id_Camaras': '3677189095748011493'}, 
	'j': {'nombre': 'LabIT3', 'serial': 'Q2LW-45P5-F593', 'interface_id_10.60.0.250': '754915887537981028'}
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
with open(r'C:\RootScripts\Lab\Input2.csv', newline='', encoding='utf-8') as csvfile:
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

"""

# POST, sirve para leer un csv previamente llenado, despues de leerlo nos sirve para setear ips estáticas atravez del dhcp.

import requests
import json
import csv

# Diccionario con la información de los sitios          #<<<<<<<<<<<<<Cambiar variable con el script3 se reemplaza el siguiente diccionario:

sitios = {
		'a': {'nombre': 'Management', 'serial': 'Q2LW-9GDX-5G8J', 'interface_id_Management': '3677189095748011588'}, 
		'b': {'nombre': 'Transit', 'serial': 'Q2LW-9GDX-5G8J', 'interface_id_Transit': '3677189095748011577'}, 
		'c': {'nombre': 'Contractors', 'serial': 'Q2LW-9GDX-5G8J', 'interface_id_Contractors': '3677189095748011584'}, 
		'd': {'nombre': 'Spare Vlan', 'serial': 'Q2LW-9GDX-5G8J', 'interface_id_Spare Vlan': '3677189095748011586'}, 
		'e': {'nombre': 'Unused ports', 'serial': 'Q2LW-9GDX-5G8J', 'interface_id_Unused ports': '3677189095748011587'}, 
		'f': {'nombre': 'NPS Guest', 'serial': 'Q2LW-9GDX-5G8J', 'interface_id_NPS Guest': '3677189095748011583'}, 
		'g': {'nombre': 'Printers', 'serial': 'Q2LW-9GDX-5G8J', 'interface_id_Printers': '3677189095748011585'}, 
		'h': {'nombre': 'NPS Radius', 'serial': 'Q2LW-9GDX-5G8J', 'interface_id_NPS Radius': '3677189095748011578'}, 
		'i': {'nombre': 'Cabling', 'serial': 'Q2LW-9GDX-5G8J', 'interface_id_Cabling': '3677189095748011579'}, 
		'j': {'nombre': 'NPS Warehouse', 'serial': 'Q2LW-9GDX-5G8J', 'interface_id_NPS Warehouse': '3677189095748011580'}, 
		'k': {'nombre': 'NPSIot', 'serial': 'Q2LW-9GDX-5G8J', 'interface_id_NPSIot': '3677189095748011581'}, 
		'l': {'nombre': 'Camaras', 'serial': 'Q2LW-9GDX-5G8J', 'interface_id_Camaras': '3677189095748011582'}
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

# Buscar la clave del interface_id en el diccionario del sitio seleccionado
interface_key = next((k for k in sitios[sitio_seleccionado] if k.startswith('interface_id_')), None)

# Verificar que se encontró una clave de interface_id válida
if interface_key is None:
    print("No se encontró una interfaz válida en el sitio seleccionado.")
    exit()

interface_id = sitios[sitio_seleccionado][interface_key]

# Construir la URL con los parámetros del sitio seleccionado
url = f"https://api.meraki.com/api/v1/devices/{serial}/switch/routing/interfaces/{interface_id}/dhcp"

# Crear una lista vacía para almacenar las asignaciones de IP fija
fixed_ip_assignments = []

# Leer el archivo CSV con codificación UTF-8
with open(r'C:/RootScripts/Birmingham/MW/NetDev.csv', newline='', encoding='utf-8') as csvfile:    #<<<<<<<<<<<<<Cambiar variable, estos son los archivos que guardan la ip vs mac address para el dhcp estatico
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
