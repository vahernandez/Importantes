
"""
import requests
import json

url = "https://api.meraki.com/api/v1/organizations/848368/devices"
payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a formato JSON con indentación para una mejor legibilidad
    formatted_response = json.dumps(response.json(), indent=2)
    
    # Abrir un archivo Notepad para escribir la salida
    with open("C:\RootScripts\output.txt", "w") as file:
        # Escribir la respuesta en el archivo
        file.write(formatted_response)
    print("La salida se ha guardado en el archivo output.txt")
else:
    print("Error:", response.status_code)
"""


"""
Se crea un csv con la lista de todos los dispositivos de la organización con el nombre de DeviceList.csv
"""
import requests
import json
import csv

url = "https://api.meraki.com/api/v1/organizations/848368/devices"
payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Obtener la respuesta en formato JSON
    devices = response.json()
    
    # Definir el nombre del archivo CSV
    csv_filename = "C:\\RootScripts\\DeviceList11.csv"
    
    # Asegurarse de que hay datos en la respuesta antes de intentar escribir el archivo
    if devices:
        # Obtener todas las claves posibles de los dispositivos
        all_keys = set()
        for device in devices:
            all_keys.update(device.keys())
        
        # Abrir un archivo CSV para escribir la salida
        with open(csv_filename, "w", newline='', encoding='utf-8') as csv_file:
            dict_writer = csv.DictWriter(csv_file, fieldnames=all_keys)
            dict_writer.writeheader()
            
            # Asegurar que todos los dispositivos tengan las mismas claves
            for device in devices:
                for key in all_keys:
                    if key not in device:
                        device[key] = None  # O podrías usar una cadena vacía "" si prefieres
                dict_writer.writerow(device)
        
        print("La salida se ha guardado en el archivo DeviceList.csv")
    else:
        print("No hay dispositivos para escribir en el archivo CSV")
else:
    print("Error:", response.status_code)
