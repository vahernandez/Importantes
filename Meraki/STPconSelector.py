import requests
import pprint

# Diccionario con los nombres de las redes y sus ID
networks = {
    "Columbus blue Building": "L_3677189095748010123",
    "Houston Bay 9": "L_609674799555294463",
    "Mexico 510": "L_609674799555294825",
    "México 520": "L_609674799555296477",
    "Columbus": "L_609674799555298933",
    "Houston Post Oak": "L_754915887537979428",
    "Appelt": "L_754915887537980062",
    "Alsip": "L_754915887537980170",
    "Butler": "L_754915887537980425",
    "Birmingham": "L_754915887537980570"
}

# Imprimir el menú de opciones
print("Seleccione la red de la que desea obtener información de STP:")
for index, (network_name, network_id) in enumerate(networks.items(), start=1):
    print(f"{index}. {network_name} ")

# Pedir al usuario que seleccione una opción
option = int(input("Ingrese el número de la red: "))

# Verificar si la opción ingresada por el usuario es válida
if option not in range(1, len(networks) + 1):
    print("Opción inválida")
else:
    # Obtener el nombre y el ID de la red seleccionada por el usuario
    selected_network_name, selected_network_id = list(networks.items())[option - 1]

    # Construir la URL de la API con el ID de la red seleccionada
    url = f"https://api.meraki.com/api/v1/networks/{selected_network_id}/switch/stp"

    # Cabeceras de la solicitud HTTP
    headers = {
        'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
    }

    # Enviar la solicitud GET a la API de Meraki
    response = requests.request("GET", url, headers=headers)

    # Imprimir la respuesta en formato JSON vertical
    pprint.pprint(response.json(), width=1)