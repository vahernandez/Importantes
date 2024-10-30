import requests
import json

url = "https://api.meraki.com/api/v1/organizations/848368/devices"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Convertir la respuesta a formato JSON con indentación para una mejor legibilidad
formatted_response = json.dumps(response.json(), indent=2)

print(formatted_response)

########################################################################################################


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
    with open("C:\RootScripts\output33.txt", "w") as file:
        # Escribir la respuesta en el archivo
        file.write(formatted_response)
    print("La salida se ha guardado en el archivo output.txt")
else:
    print("Error:", response.status_code)