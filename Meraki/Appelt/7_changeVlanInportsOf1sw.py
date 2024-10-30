
"""
import csv
import requests
import json

# Función para enviar la solicitud PUT
def enviar_solicitud(url, payload, headers):
    response = requests.put(url, headers=headers, data=json.dumps(payload))
    print(response.text)

# URL base
base_url = "https://api.meraki.com/api/v1/devices/Q4AA-GZU2-2V4B/switch/ports/"

# Cabeceras
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

# Leer el archivo CSV
with open('C:\RootScripts\PostOak\MW/PortListSw.csv', mode='r') as file:
    datos_csv = csv.reader(file)
    next(datos_csv)  # Saltar la primera fila (cabecera)
    for row in datos_csv:
        puerto_id = row[0]  # ID del puerto
        vlan = int(row[1])  # VLAN

        # Construir la URL completa con el ID del puerto
        url = base_url + f"{puerto_id}"

        # Payload con la nueva VLAN
        payload = {
            "enabled": True,
            "poeEnabled": True,
            "type": "access",
            "rstpEnabled": True,
            "stpGuard": "bpdu guard",
        }

        # Enviar la solicitud PUT
        enviar_solicitud(url, payload, headers)
"""

# POST Hay que tener los archivos debidamente llenados antes de ejecutar

import csv
import requests
import json

# Diccionario con los datos de la tabla                    # Change the next variables
switches_info = {
    "CTL_Blanking_switch": {"serial": "Q2HP-V7FC-6R92", "archivo": "CTL_Blanking_switchVlanChange.csv"},
    "IDF-A3": {"serial": "Q2KW-44RV-2ABB", "archivo": "IDF-A3VlanChange.csv"},
    "IDF-AC1": {"serial": "Q2KW-46D5-4ZY2", "archivo": "IDF-AC1VlanChange.csv"},
    "IDF-A2": {"serial": "Q2KW-46EB-F64C", "archivo": "IDF-A2VlanChange.csv"},
    "SVR_RM_Switch1": {"serial": "Q2KW-47HT-CW5P", "archivo": "SVR_RM_Switch1VlanChange.csv"},
    "IDF-B": {"serial": "Q2KW-47L5-R7LB", "archivo": "IDF-BVlanChange.csv"},
    "IDF-C": {"serial": "Q2KW-47NP-BH3B", "archivo": "IDF-CVlanChange.csv"},
    "IDF-A4": {"serial": "Q2KW-4FW7-EUWT", "archivo": "IDF-A4VlanChange.csv"},
    "IDF-A4B": {"serial": "Q2KW-4WDX-PXDJ", "archivo": "IDF-A4BVlanChange.csv"},
    "IDF-C1": {"serial": "Q2KW-4WZ9-XN6W", "archivo": "IDF-C1VlanChange.csv"},
    "SVR_RM_Switch2": {"serial": "Q2KW-5HGM-NEJT", "archivo": "SVR_RM_Switch2VlanChange.csv"},
    "Center_IDF": {"serial": "Q2KW-8DSA-RADW", "archivo": "Center_IDFVlanChange.csv"},
    "IDFAC4": {"serial": "Q2KW-AYRU-6FBX", "archivo": "IDFAC4VlanChange.csv"},
    "Appelt_Border_Switch": {"serial": "Q2LW-3D2D-LP5T", "archivo": "Appelt_Border_SwitchVlanChange.csv"}
}


# Función para enviar la solicitud PUT
def enviar_solicitud(url, payload, headers):
    response = requests.put(url, headers=headers, data=json.dumps(payload))
    print(response.text)

# Mostrar la lista numerada de switches
print("De la siguiente lista, escoge el número del switch al que quieres aplicar los cambios:")
for i, nombre in enumerate(switches_info.keys(), start=1):
    print(f"{i}\t{nombre}")

# Preguntar al usuario qué switch quiere usar
opcion = int(input("Escribe el número del switch: "))

# Obtener el nombre del switch seleccionado
switch_nombre = list(switches_info.keys())[opcion - 1]

# Verificar que el nombre del switch está en el diccionario
if switch_nombre in switches_info:
    serial = switches_info[switch_nombre]["serial"]
    archivo_csv = switches_info[switch_nombre]["archivo"]
    
    # URL base con el serial del switch seleccionado
    base_url = f"https://api.meraki.com/api/v1/devices/{serial}/switch/ports/"
    
    # Cabeceras
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
    }
    
    # Leer el archivo CSV correspondiente
    with open(f'C:/RootScripts/Appelt/MW/{archivo_csv}', mode='r') as file:    #<<<<<<<<<<<<<<<<<<<<cambiar path
        datos_csv = csv.reader(file)
        next(datos_csv)  # Saltar la primera fila (cabecera)
        for row in datos_csv:
            puerto_id = row[0]  # ID del puerto
            vlan = int(row[1])  # VLAN

            # Construir la URL completa con el ID del puerto
            url = base_url + f"{puerto_id}"

            # Payload con la nueva VLAN
            payload = {
                "enabled": True,
                "poeEnabled": True,
                "type": "access",
                "rstpEnabled": True,
                "stpGuard": "bpdu guard",
                "vlan": vlan  # Asignar la VLAN del archivo CSV
            }

            # Enviar la solicitud PUT
            enviar_solicitud(url, payload, headers)
else:
    print("Nombre de switch no encontrado en la tabla.")
