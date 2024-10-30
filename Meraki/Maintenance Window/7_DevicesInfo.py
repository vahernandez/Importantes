
"""
import requests
from pprint import pprint
url = "https://api.meraki.com/api/v1/organizations/848368/devices/statuses"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

pprint(response.json())



import requests
from pprint import pprint

# Mapeo de networkId a nombre de sitios
network_sites = {
    "L_3677189095748010123": "Columbus blue Building",
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

# Preguntar al usuario de qué sitio quiere obtener información
print("De la siguiente lista, ¿de qué sitio quieres obtener información?")
for key, value in network_sites.items():
    print(f"{key}: {value}")

selected_site = input("Ingresa el ID del sitio: ")

# Validar la entrada del usuario
if selected_site not in network_sites:
    print("El ID del sitio ingresado no es válido.")
else:
    url = f"https://api.meraki.com/api/v1/networks/{selected_site}/devices/statuses"

    payload = {}
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        print(f"Información del sitio: {network_sites[selected_site]}")
        pprint(response.json())
    else:
        print("Error al obtener la información del sitio.")


import requests
from pprint import pprint

# URL y encabezados para la solicitud
url = "https://api.meraki.com/api/v1/organizations/848368/devices/statuses"
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

# Realizar la solicitud GET
response = requests.request("GET", url, headers=headers)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    devices = response.json()
    
    # Filtrar dispositivos por networkId
    filtered_devices = [device for device in devices if device['networkId'] == 'L_609674799555294463']
    
    # Mostrar los dispositivos filtrados
    pprint(filtered_devices)
else:
    print("Error al obtener la información de los dispositivos.")



from pprint import pprint
import requests

url = "https://api.meraki.com/api/v1/organizations/848368/devices/statuses?networkIds[]=L_754915887537979428&productTypes[]=switch&productTypes[]=wireless"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

pprint(response.json())

"""


from pprint import pprint
import requests

# Tabla de networkIds y nombres
network_dict = {
    1: ("L_3677189095748010123", "Columbus blue Building"),
    2: ("L_609674799555294463", "Houston Bay 9"),
    3: ("L_609674799555294825", "Mexico 510"),
    4: ("L_609674799555296477", "México 520"),
    5: ("L_609674799555298933", "Columbus"),
    6: ("L_754915887537979428", "Houston Post Oak"),
    7: ("L_754915887537980062", "Appelt"),
    8: ("L_754915887537980170", "Alsip"),
    9: ("L_754915887537980425", "Butler"),
    10: ("L_754915887537980570", "Birmingham")
}

# Mostrar las opciones al usuario
print("Por favor, elige un número de la lista para obtener información del sitio correspondiente:")
for key, value in network_dict.items():
    print(f"{key}: {value[1]}")

# Solicitar al usuario que elija un número
num = int(input("Número: "))

# Validar la entrada del usuario
if num not in network_dict:
    print("Número no válido. Por favor, elige un número de la lista.")
else:
    # Obtener el networkId correspondiente
    network_id = network_dict[num][0]

    # URL con el networkId seleccionado
    url = f"https://api.meraki.com/api/v1/organizations/848368/devices/statuses?networkIds[]={network_id}&productTypes[]=switch&productTypes[]=wireless"

    payload = {}
    headers = {
      'Accept': 'application/json',
      'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
    }

    # Realizar la solicitud GET
    response = requests.request("GET", url, headers=headers, data=payload)

    # Verificar si la solicitud fue exitosa
    if response.status_code == 200:
        pprint(response.json())
    else:
        print("Error al obtener la información de los dispositivos.")
