import requests

# Diccionario con los datos de la tabla                         # Change the next variables
switches_info = {
    1: {"name": "CTL/Blanking switch", "serial": "Q2HP-V7FC-6R92"},
    2: {"name": "IDF-A3", "serial": "Q2KW-44RV-2ABB"},
    3: {"name": "IDF-AC1", "serial": "Q2KW-46D5-4ZY2"},
    4: {"name": "IDF-A2", "serial": "Q2KW-46EB-F64C"},
    5: {"name": "SVR RM Switch1", "serial": "Q2KW-47HT-CW5P"},
    6: {"name": "IDF-B", "serial": "Q2KW-47L5-R7LB"},
    7: {"name": "IDF-C", "serial": "Q2KW-47NP-BH3B"},
    8: {"name": "IDF-A4", "serial": "Q2KW-4FW7-EUWT"},
    9: {"name": "IDF-A4B", "serial": "Q2KW-4WDX-PXDJ"},
    10: {"name": "IDF-C1", "serial": "Q2KW-4WZ9-XN6W"},
    11: {"name": "SVR RM Switch2", "serial": "Q2KW-5HGM-NEJT"},
    12: {"name": "Center IDF", "serial": "Q2KW-8DSA-RADW"},
	13: {"name": "IDFAC4", "serial": "Q2KW-AYRU-6FBX"},
	14: {"name": "Appelt Border Switch", "serial": "Q2LW-3D2D-LP5T"}
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
