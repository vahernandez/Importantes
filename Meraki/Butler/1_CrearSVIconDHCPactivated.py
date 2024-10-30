# Este scrip no genera archivos, y sirve para crear los svis despues de haber borrado el /16 o /21 del sitio. Es un POST
import requests
import json
import time

# Configuración
api_key = '18ae04cc2813391d493c095470c859c4eced5faa'
base_url = "https://api.meraki.com/api/v1"
serial = "Q2LW-3D2D-LP5T"                             #<<<<<<<<<<<<<Cambiar variable
headers = {
    'Content-Type': 'application/json',
    'Accept': 'application/json',
    'Authorization': f'Bearer {api_key}'
}

# Datos de las interfaces           #<<<<<<<<<<<<<Cambiar variable
interfaces_info = [
    {"name": "NPS Radius", "subnet": "10.50.1.0/24", "interfaceIp": "10.50.1.1", "vlanId": "1"},
    {"name": "Servers", "subnet": "10.50.2.0/25", "interfaceIp": "10.50.2.1", "vlanId": "20"},
    {"name": "Future Users", "subnet": "10.50.2.128/25", "interfaceIp": "10.50.2.129", "vlanId": "21"},
    {"name": "NPS Warehouse", "subnet": "10.50.3.0/24", "interfaceIp": "10.50.3.1", "vlanId": "3"},
    {"name": "NPSIot", "subnet": "10.50.4.0/24", "interfaceIp": "10.50.4.1", "vlanId": "4"},
    {"name": "Camaras", "subnet": "10.50.5.0/24", "interfaceIp": "10.50.5.1", "vlanId": "50"},
    {"name": "NPS Guest", "subnet": "10.50.7.0/25", "interfaceIp": "10.50.7.1", "vlanId": "70"},
    {"name": "Printers", "subnet": "10.50.0.0/24", "interfaceIp": "10.50.0.1", "vlanId": "100"},
    {"name": "Unused ports", "subnet": "10.50.7.128/25", "interfaceIp": "10.50.7.129", "vlanId": "71"},
    {"name": "Management", "subnet": "10.50.6.0/25", "interfaceIp": "10.50.6.1", "vlanId": "60"},
    {"name": "Transit network", "subnet": "10.50.6.128/25", "interfaceIp": "10.50.6.129", "vlanId": "61"}
]

def create_interface(interface):
    create_interface_url = f"{base_url}/devices/{serial}/switch/routing/interfaces"
    create_interface_payload = json.dumps({
        "name": interface["name"],
        "subnet": interface["subnet"],
        "interfaceIp": interface["interfaceIp"],
        "multicastRouting": "disabled",
        "vlanId": interface["vlanId"],
        "ospfSettings": {
            "area": "ospfDisabled"
        }
    })

    response = requests.post(create_interface_url, headers=headers, data=create_interface_payload)
    if response.status_code != 201:
        print(f"Error al crear la interfaz: {response.text}")
        return None

    print("Interfaz creada exitosamente.")
    time.sleep(5)  # Esperar un poco para asegurar que la interfaz se haya creado correctamente
    return interface["name"]

def get_interface_id(interface_name):
    get_interfaces_url = f"{base_url}/devices/{serial}/switch/routing/interfaces"
    response = requests.get(get_interfaces_url, headers=headers)
    if response.status_code != 200:
        print(f"Error al obtener las interfaces: {response.text}")
        return None

    interfaces = response.json()
    for interface in interfaces:
        if interface['name'] == interface_name:
            return interface['interfaceId']
    return None

def configure_dhcp(interface_id):
    configure_dhcp_url = f"{base_url}/devices/{serial}/switch/routing/interfaces/{interface_id}/dhcp"
    configure_dhcp_payload = json.dumps({
        "dhcpMode": "dhcpServer",
        "dhcpLeaseTime": "1 day",
        "dnsNameserversOption": "custom",
        "dnsCustomNameservers": [
            "10.0.5.6",
            "10.0.5.7",
            "1.1.1.1"
        ],
        "bootOptionsEnabled": "false",
        "dhcpOptions": [
            {
                "code": "42",
                "type": "ip",
                "value": "10.0.5.6"
            },
            {
                "code": "4",
                "type": "ip",             #<<<<<<<<<<<<<puede ser text o ip revisar en la parte de dhcp del sitio
                "value": "10.0.5.6"
            },
            {
                "code": "15",
                "type": "text",
                "value": "nps.intranet"
            },
            {
                "code": "156",
                "type": "text",
                "value": "ftpservers=10.10.0.32, country=1, language=1"
            },
            {
                "code": "60",
                "type": "text",
                "value": "Arch:00007"
            }
        ]
    })

    response = requests.put(configure_dhcp_url, headers=headers, data=configure_dhcp_payload)
    if response.status_code != 200:
        print(f"Error al configurar DHCP: {response.text}")
        return False

    print("DHCP configurado exitosamente.")
    return True

while True:
    # Mostrar opciones al usuario
    print("Selecciona el número de la interfaz que deseas configurar:")
    for i, interface in enumerate(interfaces_info):
        print(f"{i+1}. {interface['name']}")

    # Obtener la elección del usuario
    choice = int(input("Número de la interfaz: "))
    if 1 <= choice <= len(interfaces_info):
        selected_interface = interfaces_info[choice - 1]
        interface_name = create_interface(selected_interface)
        if interface_name:
            interface_id = get_interface_id(interface_name)
            if interface_id:
                configure_dhcp(interface_id)
    else:
        print("Selección no válida.")

    # Preguntar si desea configurar otra interfaz
    continue_choice = input("¿Deseas configurar otra interfaz? (s/n): ").lower()
    if continue_choice != 's':
        break

