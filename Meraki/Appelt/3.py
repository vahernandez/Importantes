# No es API, sirve para editar información de los ids de las interfaces, no guarda información solo lo muestra en la terminal

import csv

# Definir el serial que se mantendrá igual
serial = 'Q2LW-3D2D-LP5T'                                   #<<<<<<<<<<<<<Cambiar variable del serial del switch donde estan los svis

# Ruta del archivo .txt que contiene la información
input_file = "C:/RootScripts/Appelt/MW/SVIsId.txt"                    #<<<<<<<<<<<<<Cambiar variable del path e ir a la carpeta donde se encuentra el archivo que se va a leer y borrarle la fecha y la hora 

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
