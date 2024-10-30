"""
El objetivo de este script es cambiar la respuesta del script 2 a un formato que pueda leer el script 4:


import csv

# Definir el nombre y serial que se mantendrán igual
nombre = 'LabIT3'
serial = 'Q2LW-45P5-F593'

# Ruta del archivo .txt que contiene la información
input_file = "C:/RootScripts/Lab/SVIsId.txt"

# Crear el diccionario de sitios
sitios = {}

# Leer el archivo .txt
with open(input_file, mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Usar letras para las claves del diccionario ('a', 'b', 'c', etc.)
    clave_letra = ord('a')
    
    for row in reader:
        # Crear la clave basada en la letra
        clave = chr(clave_letra)
        
        # Crear la entrada del diccionario
        sitios[clave] = {
            'nombre': nombre,
            'serial': serial,
            f"interface_id_{row['name']}": row['interfaceId']
        }
        
        # Incrementar la letra para la siguiente clave
        clave_letra += 1

# Mostrar el diccionario resultante
print(sitios)



"""



import csv

# Definir el serial que se mantendrá igual
serial = 'Q2LW-45P5-F593'

# Ruta del archivo .txt que contiene la información
input_file = "C:/RootScripts/Lab/SVIsId.txt"

# Crear el diccionario de sitios
sitios = {}

# Leer el archivo .txt
with open(input_file, mode='r') as csvfile:
    reader = csv.DictReader(csvfile)
    
    # Usar letras para las claves del diccionario ('a', 'b', 'c', etc.)
    clave_letra = ord('a')
    
    for row in reader:
        # Crear la clave basada en la letra
        clave = chr(clave_letra)
        
        # Extraer el nombre para reemplazar 'LabIT3'
        nombre = row['name']
        
        # Crear la entrada del diccionario
        sitios[clave] = {
            'nombre': nombre,
            'serial': serial,
            f"interface_id_{nombre}": row['interfaceId']
        }
        
        # Incrementar la letra para la siguiente clave
        clave_letra += 1

# Mostrar el diccionario resultante
print(sitios)
