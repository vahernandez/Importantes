import requests
import json

# Diccionario con los datos de la tabla
devices_info = {
    1: {"name": "PO Training Room", "serial": "Q4AA-GZU2-2V4B", "productType": "switch"},
    2: {"name": "PO SVR RM Switch 4", "serial": "Q2KW-Q9SK-N6L9", "productType": "switch"},
    3: {"name": "PO SVR RM Switch 3", "serial": "Q2KW-T3YN-USNU", "productType": "switch"},
    4: {"name": "PO SVR RM Switch 2", "serial": "Q2KW-RNGW-55SN", "productType": "switch"},
    5: {"name": "PO SVR RM Switch 1", "serial": "Q2KW-M4XJ-UXPJ", "productType": "switch"},
    6: {"name": "PO Server Rack", "serial": "Q2KW-HY7W-M2E2", "productType": "switch"},
    7: {"name": "PO Mail RM Switch 8", "serial": "Q2KW-T2QP-S6E3", "productType": "switch"},
    8: {"name": "PO Mail RM Switch 7", "serial": "Q2KW-SFUQ-2VZ4", "productType": "switch"},
    9: {"name": "PO Mail RM Switch 6", "serial": "Q2KW-RPFB-VJ9V", "productType": "switch"},
    10: {"name": "PO Mail RM Switch 5", "serial": "Q2KW-M4U2-PV7F", "productType": "switch"},
    11: {"name": "Bay 9", "serial": "Q2SX-8KZQ-D9L4", "productType": "switch"},
    12: {"name": "Houston Edge Switch", "serial": "Q2LW-89GD-FL29", "productType": "switch"},
    13: {"name": "ExecConference", "serial": "Q2MD-8TZM-NTCZ", "productType": "wireless"},
    14: {"name": "Walker's Office", "serial": "Q2MD-FRHW-ZSZM", "productType": "wireless"},
    15: {"name": "Main Conference", "serial": "Q2MD-PE4D-39PE", "productType": "wireless"},
    16: {"name": "Conway's Office", "serial": "Q2MD-PPMM-UAF5", "productType": "wireless"},
    17: {"name": "Courtyard", "serial": "Q2QD-6VPP-LR97", "productType": "wireless"},
    18: {"name": "AP 1", "serial": "Q2QD-T8NW-LYHR", "productType": "wireless"},
    19: {"name": "AP 2", "serial": "Q2QD-HR6Y-9AUY", "productType": "wireless"},
    20: {"name": "AP3", "serial": "Q2QD-HQR4-LA2C", "productType": "wireless"}
}

# Función para enviar la solicitud de parpadeo de LEDs
def blink_leds(serial):
    url = f"https://api.meraki.com/api/v1/devices/{serial}/blinkLeds"
    payload = json.dumps({"duration": "5"})
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
    }
    response = requests.post(url, headers=headers, data=payload)
    print(response.text)

# Preguntar al usuario qué dispositivo quiere hacer parpadear sus LEDs
print("De esta tabla, ¿a qué switch o AP quisieras que parpadeen sus LEDs de estado?")
for num, info in devices_info.items():
    print(f"{num}. {info['name']} ({info['productType']})")

device_num = int(input("Número: "))

# Verificar que el número del dispositivo está en el diccionario
if device_num in devices_info:
    serial = devices_info[device_num]["serial"]
    blink_leds(serial)
else:
    print("Número de dispositivo no encontrado en la tabla.")
