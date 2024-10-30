import requests
import json
import csv

"""
url = "https://api.meraki.com/api/v1/devices/Q2LW-453K-D784/switch/routing/interfaces/754915887537980988/dhcp"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    json_data = response.json()
    
    # Guardar la respuesta en un archivo CSV
    output_file = "C:/RootScripts/DHCPConfigForOneSVI.csv"
    with open(output_file, "w", newline="") as csvfile:
        # Escribir los datos JSON en el archivo CSV
        writer = csv.DictWriter(csvfile, fieldnames=json_data.keys())
        writer.writeheader()
        writer.writerow(json_data)
    
    print("El output ha sido guardado en el archivo 'output.csv'.")
else:
    print("Error: No se pudo obtener la respuesta del servidor.")
    
    

"""

    
    
"""   

url = "https://api.meraki.com/api/v1/devices/Q2LW-453K-D784/switch/routing/interfaces/754915887537980988/dhcp"

# El serial que se pide aqui es el del Core, el numero que acaba con 88 se consigue con el api getDeviceSwitchRoutingInterface, en este caso se trata del svi de la vlan 1


payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    json_data = response.json()
    
    # Guardar la respuesta en un archivo CSV
    output_file = "C:/RootScripts/DHCPConfigForOneSVI.csv"
    with open(output_file, "w", newline="") as csvfile:
        # Crear el escritor CSV
        writer = csv.writer(csvfile)
        
        # Escribir la primera hoja de cálculo para "reservedIpRanges"
        writer.writerow(["reservedIpRanges"])
        if "reservedIpRanges" in json_data:
            for item in json_data["reservedIpRanges"]:
                writer.writerow([item])
        else:
            writer.writerow(["No hay datos"])
        
        # Añadir una línea en blanco como separador entre las hojas de cálculo
        writer.writerow([])
        
        # Escribir la segunda hoja de cálculo para "fixedIpAssignments"
        writer.writerow(["fixedIpAssignments"])
        if "fixedIpAssignments" in json_data:
            for item in json_data["fixedIpAssignments"]:
                writer.writerow([item])
        else:
            writer.writerow(["No hay datos"])
    
    print("El output ha sido guardado en el archivo 'output.csv'.")
else:
    print("Error: No se pudo obtener la respuesta del servidor.")
    
    
"""


import requests
import csv

# Función para obtener la información del sitio seleccionado
def obtener_informacion_sitio(sitio):
    sitios = {
        'a': {'nombre': 'Mexico 510', 'serial': 'Q2LW-45P5-F593', 'interface_id_vlan1': '754915887537981028'},
        'b': {'nombre': 'México 520', 'serial': 'Q2LW-453K-D784', 'interface_id_vlan1': '754915887537980988'},
        'c': {'nombre': 'Columbus', 'serial': 'Q2LW-3CRH-W8F6', 'interface_id_vlan1': '3677189095748010627'},
        'd': {'nombre': 'Appelt', 'serial': 'Q2LW-3D2D-LP5T', 'interface_id_vlan1': '754915887537981876'},
        'e': {'nombre': 'Alsip', 'serial': 'Q2LW-87NE-L45N', 'interface_id_vlan1': '754915887537980857'},
        'f': {'nombre': 'Butler', 'serial': 'Q2LW-8A2B-5GJM', 'interface_id_vlan1': '754915887537980885'},
        'g': {'nombre': 'Birmingham', 'serial': 'Q2LW-9GDX-5G8J', 'interface_id_vlan1': '754915887537980214'}
    }
    
    # Verificar si la opción ingresada es válida
    if sitio in sitios:
        nombre_sitio = sitios[sitio]['nombre']
        serial = sitios[sitio]['serial']
        interface_id_vlan1 = sitios[sitio]['interface_id_vlan1']
        
        # Construir la URL con el serial y el interfaceId
        url = f"https://api.meraki.com/api/v1/devices/{serial}/switch/routing/interfaces/{interface_id_vlan1}/dhcp"

        # Realizar la solicitud GET a la API
        payload = {}
        headers = {
            'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
        }
        response = requests.get(url, headers=headers, data=payload)

        # Verificar si la solicitud fue exitosa
        if response.status_code == 200:
            # Convertir la respuesta a formato JSON
            json_data = response.json()
            
            # Guardar la respuesta en un archivo CSV
            output_file = f"C:/RootScripts/DHCPConfigFor{nombre_sitio}.csv"
            with open(output_file, "w", newline="") as csvfile:
                # Crear el escritor CSV
                writer = csv.writer(csvfile)
                
                # Escribir la primera hoja de cálculo para "reservedIpRanges"
                writer.writerow(["reservedIpRanges"])
                if "reservedIpRanges" in json_data:
                    for item in json_data["reservedIpRanges"]:
                        writer.writerow([item])
                else:
                    writer.writerow(["No hay datos"])
                
                # Añadir una línea en blanco como separador entre las hojas de cálculo
                writer.writerow([])
                
                # Escribir la segunda hoja de cálculo para "fixedIpAssignments"
                writer.writerow(["fixedIpAssignments"])
                if "fixedIpAssignments" in json_data:
                    for item in json_data["fixedIpAssignments"]:
                        writer.writerow([item])
                else:
                    writer.writerow(["No hay datos"])
            
            print(f"La información de red para {nombre_sitio} ha sido guardada en el archivo '{output_file}'.")
        else:
            print("Error: No se pudo obtener la respuesta del servidor.")
    else:
        print("Opción de sitio no válida. Por favor, seleccione una opción válida.")

# Preguntar al usuario por el sitio deseado
opcion_sitio = input("Por favor, seleccione el sitio del cual desea obtener la información (a-g): ")

# Llamar a la función para obtener la información del sitio seleccionado
obtener_informacion_sitio(opcion_sitio)
