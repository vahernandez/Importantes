"""import requests

url = "https://api.meraki.com/api/v1/devices/Q4CA-SPCX-FVTX/switch/ports/statuses"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

"""

"""
import requests
import json
import csv

url = "https://api.meraki.com/api/v1/devices/Q2KW-44RV-2ABB/switch/ports/statuses"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    json_data = response.json()
    
    # Guardar la respuesta en un archivo de texto en formato JSON
    with open("C:\RootScripts\statusPort.csv", "w") as file:
        json.dump(json_data, file, indent=4)
    
    print("El output ha sido guardado en el archivo 'output.json'.")
else:
    print("Error: No se pudo obtener la respuesta del servidor.")


"""

"""
import requests
import csv

url = "https://api.meraki.com/api/v1/devices/Q2KW-44RV-2ABB/switch/ports/statuses"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    json_data = response.json()
    
    # Crear un archivo CSV para escribir la información
    with open("C:\\RootScripts\\statusPort.csv", "w", newline="") as csvfile:
        # Crear el escritor CSV
        writer = csv.writer(csvfile)
        
        # Escribir el encabezado del CSV
        writer.writerow(["portId", "enabled", "status", "isUplink", "cdpPlatform", "cdpAddress", "lldpSystemName", "lldpChassisId", "clientCount"])
        
        # Iterar sobre cada puerto en la respuesta JSON
        for port_data in json_data:
            # Obtener los valores de los campos específicos
            port_id = port_data.get("portId", "")
            enabled = port_data.get("enabled", "")
            status = port_data.get("status", "")
            is_uplink = port_data.get("isUplink", "")
            cdp_platform = port_data.get("cdpPlatform", "")
            cdp_address = port_data.get("cdpAddress", "")
            lldp_system_name = port_data.get("lldpSystemName", "")
            lldp_chassis_id = port_data.get("lldpChassisId", "")
            client_count = port_data.get("clientCount", "")
            
            # Escribir los datos del puerto en una fila del CSV
            writer.writerow([port_id, enabled, status, is_uplink, cdp_platform, cdp_address, lldp_system_name, lldp_chassis_id, client_count])
    
    print("El output ha sido guardado en el archivo 'statusPort.csv'.")
else:
    print("Error: No se pudo obtener la respuesta del servidor.")
"""



"""
import requests
import csv

url = "https://api.meraki.com/api/v1/devices/Q2KW-44RV-2ABB/switch/ports/statuses"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    json_data = response.json()
    
    # Crear un archivo CSV para escribir la información
    with open("C:\\RootScripts\\statusPort.csv", "w", newline="") as csvfile:
        # Crear el escritor CSV
        writer = csv.writer(csvfile)
        
        # Escribir el encabezado del CSV
        writer.writerow(["portId", "enabled", "status", "isUplink", "cdpPlatform"])
        
        # Iterar sobre cada puerto en la respuesta JSON
        for port_data in json_data:
            # Obtener los valores de los campos específicos
            port_id = port_data.get("portId", "")
            enabled = port_data.get("enabled", "")
            status = port_data.get("status", "")
            is_uplink = port_data.get("isUplink", "")
            cdp_platform = port_data.get("cdp"[1], "")
            
            # Escribir los datos del puerto en una fila del CSV
            writer.writerow([port_id, enabled, status, is_uplink, cdp_platform])
    
    print("El output ha sido guardado en el archivo 'statusPort.csv'.")
else:
    print("Error: No se pudo obtener la respuesta del servidor.")

"""

import requests
import csv

url = "https://api.meraki.com/api/v1/devices/Q2KW-8DSA-RADW/switch/ports/statuses"

payload = {}
headers = {
  'X-Cisco-Meraki-API-Key': '18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa
if response.status_code == 200:
    # Convertir la respuesta a formato JSON
    json_data = response.json()
    
    # Crear un archivo CSV para escribir la información
    with open("C:\\RootScripts\\statusPort.csv", "w", newline="") as csvfile:
        # Crear el escritor CSV
        writer = csv.writer(csvfile)
        
        # Escribir el encabezado del CSV
        writer.writerow(["portId", "enabled", "status", "isUplink", "errors", "warnings", "speed", "duplex", "usageInKb_total", "usageInKb_sent", "usageInKb_recv", "cdp_platform", "cdp_address", "lldp_system_name", "lldp_chassisId", "clientCount"])
        
        # Iterar sobre cada puerto en la respuesta JSON
        for port_data in json_data:
            # Obtener los valores de los campos específicos
            port_id = port_data.get("portId", "")
            enabled = port_data.get("enabled", "")
            status = port_data.get("status", "")
            is_uplink = port_data.get("isUplink", "")
            errors = port_data.get("errors", "")
            warnings = port_data.get("warnings", "")
            speed = port_data.get("speed", "")
            duplex = port_data.get("duplex", "")
            usage_total = port_data.get("usageInKb", {}).get("total", "")
            usage_sent = port_data.get("usageInKb", {}).get("sent", "")
            usage_recv = port_data.get("usageInKb", {}).get("recv", "")
            
            # Obtener los valores del diccionario "cdp" si están disponibles
            cdp = port_data.get("cdp", {})
            cdp_platform = cdp.get("platform", "")
            cdp_address = cdp.get("address", "")
            
            # Obtener los valores del diccionario "lldp" si están disponibles
            lldp = port_data.get("lldp", {})
            lldp_system_name = lldp.get("systemName", "")
            lldp_chassisId = lldp.get("chassisId", "")
            
            # Otros campos
            client_count = port_data.get("clientCount", "")
            
            # Escribir los datos del puerto en una fila del CSV
            writer.writerow([port_id, enabled, status, is_uplink, errors, warnings, speed, duplex, usage_total, usage_sent, usage_recv, cdp_platform, cdp_address, lldp_system_name, lldp_chassisId, client_count])
    
    print("El output ha sido guardado en el archivo 'statusPort.csv'.")
else:
    print("Error: No se pudo obtener la respuesta del servidor.")



