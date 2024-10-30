import requests

# Diccionario con los datos de la tabla
switches_info = {
    1: {"name": "PO Mail RM Switch 8", "serial": "Q2KW-T2QP-S6E3"},
    2: {"name": "PO Mail RM Switch 7", "serial": "Q2KW-SFUQ-2VZ4"},
    3: {"name": "PO Mail RM Switch 6", "serial": "Q2KW-RPFB-VJ9V"},
    4: {"name": "PO SVR RM Switch 1", "serial": "Q2KW-M4XJ-UXPJ"},
    5: {"name": "PO Training Room", "serial": "Q4AA-GZU2-2V4B"},
    6: {"name": "PO SVR RM Switch 2", "serial": "Q2KW-RNGW-55SN"},
    7: {"name": "PO SVR RM Switch 4", "serial": "Q2KW-Q9SK-N6L9"},
    8: {"name": "PO Mail RM Switch 5", "serial": "Q2KW-M4U2-PV7F"},
    9: {"name": "PO SVR RM Switch 3", "serial": "Q2KW-T3YN-USNU"},
    10: {"name": "PO Server Rack", "serial": "Q2KW-HY7W-M2E2"},
    11: {"name": "Bay 9", "serial": "Q2SX-8KZQ-D9L4"},
    12: {"name": "Houston Edge Switch", "serial": "Q2LW-89GD-FL29"}
}

# Función para enviar la solicitud de reinicio
def enviar_reset(serial):
    url = f"https://api.meraki.com/api/v1/devices/{serial}/reboot"
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
    }
    response = requests.post(url, headers=headers)
    if response.status_code == 200:
        print(f"Reinicio exitoso del dispositivo con serial {serial}")
    else:
        print(f"Error al reiniciar el dispositivo con serial {serial}: {response.text}")

# Reiniciar todos los switches en el diccionario
for info in switches_info.values():
    enviar_reset(info["serial"])
