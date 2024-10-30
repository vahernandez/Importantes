import requests

# URL y headers para la solicitud
url = "https://api.meraki.com/api/v1/devices/Q2LW-3D2D-LP5T/switch/routing/interfaces"
headers = {
    'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

# Realizar la solicitud GET
response = requests.get(url, headers=headers)

# Parsear la respuesta JSON
data = response.json()

# Filtrar y mostrar solo los campos específicos para cada interfaz
for interface in data:
    filtered_data = {
        "interfaceId": interface.get("interfaceId"),
        "name": interface.get("name"),
        "interfaceIp": interface.get("interfaceIp"),
        "multicastRouting": interface.get("multicastRouting"),
        "vlanId": interface.get("vlanId"),
        "ospfSettings": {
            "area": interface.get("ospfSettings", {}).get("area")
        }
    }
    print(filtered_data)
