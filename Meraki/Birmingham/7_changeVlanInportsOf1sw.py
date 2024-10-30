
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

# Diccionario con los datos de la tabla               #<<<<<<<<<<<<<<<<<<<<<<<<<<<  Cambiar el nombre de cada switch y su serial
switches_info = {
    "Bay9_portVlanChange": {"serial": "Q2SX-8KZQ-D9L4", "archivo": "Bay9_portVlanChange.csv"},
    "HoustonEdge_portVlanChange": {"serial": "Q2LW-89GD-FL29", "archivo": "HoustonEdge_portVlanChange.csv"},
    "POMailRMSwitch1_portVlanChange": {"serial": "Q2KW-M4XJ-UXPJ", "archivo": "POMailRMSwitch1_portVlanChange.csv"},
    "POMailRMSwitch2_portVlanChange": {"serial": "Q2KW-RNGW-55SN", "archivo": "POMailRMSwitch2_portVlanChange.csv"},
    "POMailRMSwitch3_portVlanChange": {"serial": "Q2KW-T3YN-USNU", "archivo": "POMailRMSwitch3_portVlanChange.csv"},
    "POMailRMSwitch4_portVlanChange": {"serial": "Q2KW-Q9SK-N6L9", "archivo": "POMailRMSwitch4_portVlanChange.csv"},
    "POMailRMSwitch5_portVlanChange": {"serial": "Q2KW-M4U2-PV7F", "archivo": "POMailRMSwitch5_portVlanChange.csv"},
    "POMailRMSwitch6_portVlanChange": {"serial": "Q2KW-RPFB-VJ9V", "archivo": "POMailRMSwitch6_portVlanChange.csv"},
    "POMailRMSwitch7_portVlanChange": {"serial": "Q2KW-SFUQ-2VZ4", "archivo": "POMailRMSwitch7_portVlanChange.csv"},
    "POMailRMSwitch8_portVlanChange": {"serial": "Q2KW-T2QP-S6E3", "archivo": "POMailRMSwitch8_portVlanChange.csv"},
    "POServerRack_portVlanChange": {"serial": "Q2KW-HY7W-M2E2", "archivo": "POServerRack_portVlanChange.csv"},
    "POTrainingRoom_portVlanChange": {"serial": "Q4AA-GZU2-2V4B", "archivo": "POTrainingRoom_portVlanChange.csv"}
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
    with open(f'C:/RootScripts/Birmingham/MW/{archivo_csv}', mode='r') as file:      # <<<<<<<<<<<cambiar el path
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
