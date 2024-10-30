# GET, sirve para obtener todos los dispositivos de la red en un archivo csv
import requests
import csv

# URL para obtener los dispositivos de la organización
url = "https://api.meraki.com/api/v1/organizations/848368/devices"

# Diccionario para mapear los 'networkId' con los nombres de los sitios
sites = {
    "L_3677189095748010123": "Columbus Blue Building",
    "L_609674799555294463": "Houston Bay 9",
    "L_609674799555294825": "Mexico 510",
    "L_609674799555296477": "México 520",
    "L_609674799555298933": "Columbus",
    "L_754915887537979428": "Houston Post Oak",
    "L_754915887537980062": "Appelt",
    "L_754915887537980170": "Alsip",
    "L_754915887537980425": "Butler",
    "L_754915887537980570": "Birmingham"
}

# Definir encabezados
headers = {
    'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

# Realizar la solicitud a la API
response = requests.get(url, headers=headers)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    devices = response.json()  # Convertir la respuesta en JSON

    # Crear archivo CSV para guardar la información
    with open('C:/RootScripts/Appelt/Inventory.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        # Escribir encabezados
        writer.writerow(['Site', 'Device Name', 'Serial', 'MAC', 'Model', 'LAN IP', 'Firmware', 'NetworkId'])

        # Procesar cada dispositivo en la respuesta
        for device in devices:
            network_id = device.get('networkId', 'Unknown')  # Obtener el networkId
            site_name = sites.get(network_id, 'Unknown Site')  # Asignar el nombre del sitio según el networkId

            # Escribir la información del dispositivo en el archivo CSV
            writer.writerow([
                site_name,
                device.get('name', 'N/A'),
                device.get('serial', 'N/A'),
                device.get('mac', 'N/A'),
                device.get('model', 'N/A'),
                device.get('lanIp', 'N/A'),
                device.get('firmware', 'N/A'),
                device.get('networkId', 'N/A')
            ])

    print("Información guardada en 'devices_by_site.csv'")
else:
    print(f"Error al hacer la solicitud: {response.status_code}")
