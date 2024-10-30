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
    
 ############################################################################################################################################################   

# Con este scrip podemos ver cuales son los ips-macs registrado para dhcp de la interfaz svi legacy con el nombre DHCPConfigFor + el nombre del sitio, es importante no tener un archivo abierto con este nombre
# Sacar los ids de los svis con el scrip de InterfaceIdForCoreSw
# si algun Id no esta, se puede agregar.

import requests
import csv

# Función para obtener la información del sitio seleccionado
def obtener_informacion_sitio(sitio):
    sitios = {                                                                                                       #<<<<<<<<<<<<<Cuando pegamos este dicc del scrip previo, checar la identación de esta linea
		'a': {'nombre': 'Printers', 'serial': 'Q2LW-45P5-F593', 'interface_id_Printers': '3677189095748011490'}, 
		'b': {'nombre': 'Contractors', 'serial': 'Q2LW-45P5-F593', 'interface_id_Contractors': '3677189095748011492'}, 
		'c': {'nombre': 'Spare Vlan', 'serial': 'Q2LW-45P5-F593', 'interface_id_Spare Vlan': '3677189095748011494'}, 
		'd': {'nombre': 'Unused ports', 'serial': 'Q2LW-45P5-F593', 'interface_id_Unused ports': '3677189095748011495'}, 
		'e': {'nombre': 'NPS Guest', 'serial': 'Q2LW-45P5-F593', 'interface_id_NPS Guest': '3677189095748011491'}, 
		'f': {'nombre': 'Cabling', 'serial': 'Q2LW-45P5-F593', 'interface_id_Cabling': '3677189095748011487'}, 
		'g': {'nombre': 'NPS Warehouse', 'serial': 'Q2LW-45P5-F593', 'interface_id_NPS Warehouse': '3677189095748011488'}, 
		'h': {'nombre': 'NPSIot', 'serial': 'Q2LW-45P5-F593', 'interface_id_NPSIot': '3677189095748011489'}, 
		'i': {'nombre': 'Camaras', 'serial': 'Q2LW-45P5-F593', 'interface_id_Camaras': '3677189095748011493'}, 
		'j': {'nombre': '10.60.0.250', 'serial': 'Q2LW-45P5-F593', 'interface_id_10.60.0.250': '754915887537981028'}
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
            output_file = f"C:/RootScripts/PostOak/MW/DHCPConfigFor{nombre_sitio}.csv"              #<<<<<<<<<<<<<Cambiar variable
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
opcion_sitio = input("Por favor, seleccione el sitio del cual desea obtener la información (a-h): ")

# Llamar a la función para obtener la información del sitio seleccionado
obtener_informacion_sitio(opcion_sitio)



"""
## GET para obtener o hacer un backup de como esta el dhcp estatico de un svi en específico

import requests
import csv

# Función para obtener la información del sitio seleccionado      # el siguient diccionario se cambia con el output del script 5
def obtener_informacion_sitio(sitio):

    sitios = {
		'a': {'nombre': 'BHMDHCP', 'serial': 'Q2LW-9GDX-5G8J', 'interface_id_BHMDHCP': '754915887537980214'}
}

    # Verificar si la opción ingresada es válida
    if sitio in sitios:
        nombre_sitio = sitios[sitio]['nombre']
        serial = sitios[sitio]['serial']
        
        # Obtener la clave del interface_id correspondiente al sitio
        interface_id_key = f'interface_id_{nombre_sitio}'
        interface_id = sitios[sitio].get(interface_id_key)
        
        if interface_id:
            # Construir la URL con el serial y el interfaceId
            url = f"https://api.meraki.com/api/v1/devices/{serial}/switch/routing/interfaces/{interface_id}/dhcp"

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
                output_file = f"C:/RootScripts/Birmingham/MW/DHCPConfigFor{nombre_sitio}.csv"                #<<<<< Se cambia variable en este caso el path
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
            print(f"No se encontró el interface ID para el sitio '{nombre_sitio}'.")
    else:
        print("Opción de sitio no válida. Por favor, seleccione una opción válida.")

# Preguntar al usuario por el sitio deseado
opcion_sitio = input("Por favor, seleccione el sitio del cual desea obtener la información (a-h): ")

# Llamar a la función para obtener la información del sitio seleccionado
obtener_informacion_sitio(opcion_sitio)
