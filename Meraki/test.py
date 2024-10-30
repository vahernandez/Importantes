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
    
    # Filtrar los dispositivos para seleccionar solo aquellos con "productType": "switch"
    switch_devices = [device for device in devices if device.get("productType") == "switch"]
    
    # Crear un archivo CSV y escribir los datos
    with open("C:\RootScripts\switch_devices.csv", "w", newline="") as csvfile:
        fieldnames = ['name', 'lanIp']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for device in switch_devices:
            writer.writerow({'name': device.get("name"), 'lanIp': device.get("lanIp")})
    
    print("Los datos se han guardado en el archivo switch_devices.csv")
else:
    print("Error:", response.status_code)