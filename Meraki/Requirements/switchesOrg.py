"""
import requests

url = "https://api.meraki.com/api/v1/organizations/848368/devices?productTypes=switch"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)

"""
"""
#######################################################################

import requests
import pprint

url = "https://api.meraki.com/api/v1/organizations/848368/devices?productTypes[]=switch"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener la lista de switches del JSON
    switches = response.json()
    
    # Iterar sobre cada switch y mostrar solo la información específica
    for switch in switches:
        print("Name:", switch['name'])
        print("Model:", switch['model'])
        print("LAN IP:", switch['lanIp'])
        print("LAN IP:", switch['lanIp'])
        print("Serial: ", switch['serial'])
        print("Network: ", switch['networkId'])
else:
    # Si la solicitud no fue exitosa, imprimir el mensaje de error
    print("Error:", response.text)

"""
"""

import requests
from tabulate import tabulate

# Diccionario con los nombres de los sitios y sus IDs de organización
sites = {
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

# Lista para almacenar la información de los switches de cada sitio
site_switches = []

# Realizar una solicitud para cada sitio y obtener la información de los switches
for site_name, org_id in sites.items():
    url = f"https://api.meraki.com/api/v1/organizations/{org_id}/devices?productTypes[]=switch"
    headers = {
        'Accept': 'application/json',
        'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
    }
    response = requests.request("GET", url, headers=headers)
    if response.status_code == 200:
        switches = response.json()
        for switch in switches:
            site_switches.append([site_name, switch['name'], switch['model'], switch['lanIp']])

# Mostrar la información en forma de tabla
print(tabulate(site_switches, headers=["Site", "Switch Name", "Model", "LAN IP"], tablefmt="grid"))

"""
"""
import requests

# Definir la relación de sitios y sus IDs de organización
sitios = {
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

# Función para obtener el ID de organización de un sitio
def obtener_id_organizacion(sitio):
    return sitios.get(sitio, "")

# Función de ordenamiento personalizada para ordenar por sitios
def ordenar_por_sitios(switch):
    nombre_switch = switch['name']
    if nombre_switch:
        sitio_switch = nombre_switch.split()[0]
        return obtener_id_organizacion(sitio_switch)
    else:
        return ""

url = "https://api.meraki.com/api/v1/organizations/848368/devices?productTypes[]=switch"

payload = {}
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener la lista de switches del JSON
    switches = response.json()

    # Ordenar los switches por sitios
    switches_ordenados = sorted(switches, key=ordenar_por_sitios)
    
    # Iterar sobre cada switch y mostrar solo la información específica
    for switch in switches_ordenados:
        print("Name:", switch['name'])
        print("Model:", switch['model'])
        print("LAN IP:", switch['lanIp'])
        print("Serial:", switch['serial'])
        print("Network:", switch['networkId'])
        print()
else:
    # Si la solicitud no fue exitosa, imprimir el mensaje de error
    print("Error:", response.text)
    
    
"""


"""
import requests

url = "https://api.meraki.com/api/v1/organizations/848368/devices?productTypes[]=switch"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener la lista de switches del JSON
    switches = response.json()
    
    # Filtrar los switches para excluir los que no tienen valor en "Name"
    switches_filtrados = [switch for switch in switches if switch.get('name')]
    
    # Ordenar switches filtrados por la red a la que pertenecen
    switches_ordenados = sorted(switches_filtrados, key=lambda x: x['networkId'])
    
    # Iterar sobre cada switch y mostrar solo la información específica
    for switch in switches_ordenados:
        print("Name:", switch['name'])
        print("Model:", switch['model'])
        print("LAN IP:", switch['lanIp'])
        print("Serial: ", switch['serial'])
        print("Network: ", switch['networkId'])
        print()
else:
    # Si la solicitud no fue exitosa, imprimir el mensaje de error
    print("Error:", response.text)


"""

"""

import requests

url = "https://api.meraki.com/api/v1/organizations/848368/devices?productTypes[]=switch"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

# Diccionario para mapear los valores de "Network" a los nombres de los sitios
network_mapping = {
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

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener la lista de switches del JSON
    switches = response.json()
    
    # Filtrar los switches para excluir los que no tienen valor en "Name"
    switches_filtrados = [switch for switch in switches if switch.get('name')]
    
    # Ordenar switches filtrados por la red a la que pertenecen
    switches_ordenados = sorted(switches_filtrados, key=lambda x: x['networkId'])
    
    # Iterar sobre cada switch y mostrar solo la información específica
    for switch in switches_ordenados:
        print("Name:", switch['name'])
        print("Model:", switch['model'])
        print("LAN IP:", switch['lanIp'])
        print("Serial: ", switch['serial'])
        network_id = switch['networkId']
        site_name = network_mapping.get(network_id, "Unknown Site")
        print("Network:", site_name)
        print()
else:
    # Si la solicitud no fue exitosa, imprimir el mensaje de error
    print("Error:", response.text)

"""

"""
import requests

url = "https://api.meraki.com/api/v1/organizations/848368/devices?productTypes[]=switch"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

# Diccionario para mapear los valores de "Network" a los nombres de los sitios
network_mapping = {
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

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener la lista de switches del JSON
    switches = response.json()
    
    # Filtrar los switches para excluir los que no tienen valor en "Name"
    switches_filtrados = [switch for switch in switches if switch.get('name')]
    
    # Ordenar switches filtrados por la red a la que pertenecen
    switches_ordenados = sorted(switches_filtrados, key=lambda x: x['networkId'])
    
    # Iterar sobre cada switch y mostrar solo la información específica
    for switch in switches_ordenados:
        print("Name:", switch['name'])
        print("Model:", switch['model'])
        print("LAN IP:", switch['lanIp'])
        print("Serial: ", switch['serial'])
        network_id = switch['networkId']
        site_name = network_mapping.get(network_id, "Unknown Site")
        print("Network:", site_name)
        print()
else:
    # Si la solicitud no fue exitosa, imprimir el mensaje de error
    print("Error:", response.text)
    
"""

"""
import requests
from tabulate import tabulate

url = "https://api.meraki.com/api/v1/organizations/848368/devices?productTypes[]=switch"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

# Diccionario para mapear los valores de "Network" a los nombres de los sitios
network_mapping = {
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

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener la lista de switches del JSON
    switches = response.json()
    
    # Filtrar los switches para excluir los que no tienen valor en "Name"
    switches_filtrados = [switch for switch in switches if switch.get('name')]
    
    # Ordenar switches filtrados por la red a la que pertenecen
    switches_ordenados = sorted(switches_filtrados, key=lambda x: x['networkId'])
    
    # Crear una lista de listas para almacenar los datos de los interruptores
    table_data = []
    for switch in switches_ordenados:
        network_id = switch['networkId']
        site_name = network_mapping.get(network_id, "Unknown Site")
        table_data.append([switch['name'], switch['model'], switch['lanIp'], site_name])
    
    # Mostrar los datos en forma de tabla usando tabulate
    headers = ["Name", "Model", "LAN IP", "Site"]
    print(tabulate(table_data, headers=headers, tablefmt="grid"))
else:
    # Si la solicitud no fue exitosa, imprimir el mensaje de error
    print("Error:", response.text)

"""

"""
import requests
from tabulate import tabulate

url = "https://api.meraki.com/api/v1/organizations/848368/devices?productTypes[]=switch"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

# Diccionario para mapear los valores de "Network" a los nombres de los sitios
network_mapping = {
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

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener la lista de switches del JSON
    switches = response.json()
    
    # Filtrar los switches para excluir los que no tienen valor en "Name"
    switches_filtrados = [switch for switch in switches if switch.get('name')]
    
    # Ordenar switches filtrados por la red a la que pertenecen
    switches_ordenados = sorted(switches_filtrados, key=lambda x: x['networkId'])
    
    # Crear un diccionario para almacenar el número de switches por sitio
    num_switches_por_sitio = {}
    
    # Iterar sobre cada switch y mostrar solo la información específica
    for switch in switches_ordenados:
        network_id = switch['networkId']
        site_name = network_mapping.get(network_id, "Unknown Site")
        
        # Incrementar el contador de switches para este sitio
        num_switches_por_sitio[site_name] = num_switches_por_sitio.get(site_name, 0) + 1
        
        # Agregar el número de switch como una nueva columna
        switch['numSwitch'] = num_switches_por_sitio[site_name]
        
    # Mostrar encabezados de la tabla
    headers = ["Name", "Model", "LAN IP", "Site", "Num Switchs"]
    
    # Crear una lista de listas con los datos de los switches
    data = [[switch['name'], switch['model'], switch['lanIp'], network_mapping.get(switch['networkId'], "Unknown Site"), switch['numSwitch']] for switch in switches_ordenados]
    
    # Imprimir la tabla utilizando tabulate
    print(tabulate(data, headers=headers, tablefmt="grid"))

else:
    # Si la solicitud no fue exitosa, imprimir el mensaje de error
    print("Error:", response.text)

"""

"""
import requests
from tabulate import tabulate

url = "https://api.meraki.com/api/v1/organizations/848368/devices?productTypes[]=switch"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

# Diccionario para mapear los valores de "Network" a los nombres de los sitios
network_mapping = {
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

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener la lista de switches del JSON
    switches = response.json()
    
    # Filtrar los switches para excluir los que no tienen valor en "Name"
    switches_filtrados = [switch for switch in switches if switch.get('name')]
    
    # Ordenar switches filtrados por la red a la que pertenecen
    switches_ordenados = sorted(switches_filtrados, key=lambda x: x['networkId'])
    
    # Crear un diccionario para almacenar el número de switches por sitio
    num_switches_por_sitio = {}
    
    # Iterar sobre cada switch y mostrar solo la información específica
    for switch in switches_ordenados:
        network_id = switch['networkId']
        site_name = network_mapping.get(network_id, "Unknown Site")
        
        # Obtener el contador de switches para este sitio
        num_switches = num_switches_por_sitio.get(site_name, 0)
        
        # Incrementar el contador de switches solo si el sitio es diferente al del switch anterior
        if switch.get('name') and switch.get('networkId'):
            if 'previousSite' not in switch or num_switches_por_sitio.get(switch['previousSite'], "Unknown Site") != site_name:
                num_switches += 1

        
        # Actualizar el contador de switches para este sitio
        num_switches_por_sitio[site_name] = num_switches
        
        # Agregar el número de switch como una nueva columna
        switch['numSwitch'] = num_switches
        
        # Almacenar el sitio anterior para el próximo switch
        switch['previousSite'] = site_name
    
    # Filtrar switches con firmware "Not running configured version"
    switches_filtrados = [switch for switch in switches_ordenados if switch['firmware'] != "Not running configured version"]
    
    # Mostrar encabezados de la tabla
    headers = ["Name", "Model", "LAN IP", "Site", "Num Switchs", "Serial", "Firmware"]
    
    # Crear una lista de listas con los datos de los switches
    data = [[switch['name'], switch['model'], switch['lanIp'], network_mapping.get(switch['networkId'], "Unknown Site"), switch['numSwitch'], switch['serial'], switch['firmware']] for switch in switches_filtrados]
    
    # Imprimir la tabla utilizando tabulate
    print(tabulate(data, headers=headers, tablefmt="grid"))

else:
    # Si la solicitud no fue exitosa, imprimir el mensaje de error
    print("Error:", response.text)







import requests
from tabulate import tabulate

url = "https://api.meraki.com/api/v1/organizations/848368/devices?productTypes[]=switch"

payload = {}
headers = {
  'Accept': 'application/json',
  'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

# Diccionario para mapear los valores de "Network" a los nombres de los sitios
network_mapping = {
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

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener la lista de switches del JSON
    switches = response.json()
    
    # Filtrar los switches para excluir los que no tienen valor en "Name"
    switches_filtrados = [switch for switch in switches if switch.get('name')]
    
    # Ordenar switches filtrados por la red a la que pertenecen
    switches_ordenados = sorted(switches_filtrados, key=lambda x: x['networkId'])
    
    # Crear un diccionario para almacenar el número de switches por sitio
    num_switches_por_sitio = {}
    
    # Iterar sobre cada switch y mostrar solo la información específica
    for switch in switches_ordenados:
        network_id = switch['networkId']
        site_name = network_mapping.get(network_id, "Unknown Site")
        
        # Obtener el contador de switches para este sitio
        num_switches = num_switches_por_sitio.get(site_name, 0)
        
        # Incrementar el contador de switches solo si el sitio es diferente al del switch anterior
        if switch.get('name') and switch.get('networkId'):
            if 'previousSite' not in switch or num_switches_por_sitio.get(switch['previousSite'], "Unknown Site") != site_name:
                num_switches += 1
        
        # Actualizar el contador de switches para este sitio
        num_switches_por_sitio[site_name] = num_switches
        
        # Agregar el número de switch como una nueva columna
        switch['numSwitch'] = num_switches
        
        # Almacenar el sitio anterior para el próximo switch
        switch['previousSite'] = site_name
    
    # Filtrar switches con firmware "Not running configured version"
    switches_filtrados = [switch for switch in switches_ordenados if switch['firmware'] != "Not running configured version"]
    
    # Mostrar encabezados de la tabla
    headers = ["Name", "Model", "LAN IP", "Site", "Num Switchs", "Serial", "Firmware"]
    
    # Crear una lista de listas con los datos de los switches
    data = [[switch['name'], switch['model'], switch['lanIp'], network_mapping.get(switch['networkId'], "Unknown Site"), switch['numSwitch'], switch['serial'], switch['firmware']] for switch in switches_filtrados]
    
    # Imprimir la tabla utilizando tabulate
    print(tabulate(data, headers=headers, tablefmt="grid"))
    
    # Preguntar al usuario qué switch le gustaría obtener información
    serial_input = input("Por favor, ingrese el número de serie del switch del que desea obtener información: ")
    print("Muchas gracias, vamos a revisar la información del switch que quieres.")

else:
    # Si la solicitud no fue exitosa, imprimir el mensaje de error
    print("Error:", response.text)


"""













import requests

url = "https://api.meraki.com/api/v1/organizations/848368/devices?productTypes[]=switch"

payload = {}
headers = {
    'Accept': 'application/json',
    'Authorization': 'Bearer 18ae04cc2813391d493c095470c859c4eced5faa'
}

# Diccionario para mapear los valores de "Network" a los nombres de los sitios
network_mapping = {
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

response = requests.request("GET", url, headers=headers, data=payload)

# Verificar si la solicitud fue exitosa (código de estado 200)
if response.status_code == 200:
    # Obtener la lista de switches del JSON
    switches = response.json()
    
    # Filtrar los switches para excluir los que no tienen valor en "Name"
    switches_filtrados = [switch for switch in switches if switch.get('name')]
    
    # Ordenar switches filtrados por la red a la que pertenecen
    switches_ordenados = sorted(switches_filtrados, key=lambda x: x['networkId'])
    
    # Crear un diccionario para almacenar el número de switches por sitio
    num_switches_por_sitio = {}
    
    # Iterar sobre cada switch y mostrar solo la información específica
    for switch in switches_ordenados:
        network_id = switch['networkId']
        site_name = network_mapping.get(network_id, "Unknown Site")
        
        # Obtener el contador de switches para este sitio
        num_switches = num_switches_por_sitio.get(site_name, 0)
        
        # Incrementar el contador de switches solo si el sitio es diferente al del switch anterior
        if switch.get('name') and switch.get('networkId'):
            if 'previousSite' not in switch or num_switches_por_sitio.get(switch['previousSite'], "Unknown Site") != site_name:
                num_switches += 1
        
        # Actualizar el contador de switches para este sitio
        num_switches_por_sitio[site_name] = num_switches
        
        # Agregar el número de switch como una nueva columna
        switch['numSwitch'] = num_switches
        
        # Almacenar el sitio anterior para el próximo switch
        switch['previousSite'] = site_name
    
    # Filtrar switches con firmware "Not running configured version"
    switches_filtrados = [switch for switch in switches_ordenados if switch['firmware'] != "Not running configured version"]
    
    # Mostrar encabezados de la tabla
    print("{:<25} {:<15} {:<15} {:<20} {:<10} {:<20} {:<25}".format("Name", "Model", "LAN IP", "Site", "# Switches", "Serial", "Firmware"))
    print("="*130)
    
    # Crear una lista de listas con los datos de los switches
    for switch in switches_filtrados:
        print("{:<25} {:<15} {:<15} {:<20} {:<10} {:<20} {:<25}".format(
            switch['name'],
            switch['model'],
            switch['lanIp'],
            network_mapping.get(switch['networkId'], "Unknown Site"),
            switch['numSwitch'],
            switch['serial'],
            switch['firmware']
        ))
    
    # Preguntar al usuario qué switch le gustaría obtener información
    serial_input = input("Por favor, ingrese el número de serie del switch del que desea obtener información: ")
    print("Muchas gracias, vamos a revisar la información del switch que quieres.")

else:
    # Si la solicitud no fue exitosa, imprimir el mensaje de error
    print("Error:", response.text)
