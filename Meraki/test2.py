import requests
import csv

url = "https://api.meraki.com/api/v1/organizations/848368/devices"
payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    devices = response.json()
    
    # Crear un archivo CSV y escribir los datos
    with open("C:\RootScripts\switch_devices2.csv", "w", newline="") as csvfile:
        fieldnames = ['name', 'lanIp', 'networkId']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for device in devices:
            # Verificar si el dispositivo es un switch y su networkId es "L_609674799555294825"
            if device.get("productType") == "switch":
                network_id = device.get("networkId")
                if network_id == "L_609674799555294825":
                    writer.writerow({'name': device.get("name"), 'lanIp': device.get("lanIp"), 'networkId': network_id})
    
    print("Los datos se han guardado en el archivo switch_devices2.csv")
else:
    print("Error:", response.status_code)