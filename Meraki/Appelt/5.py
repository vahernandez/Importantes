# No es API, sirve para editar información de los ids de las interfaces, no guarda información solo lo muestra en la terminal, sirve para copiar el resultado y ponerlo en el siguiente script

import csv

# Definir el serial que se mantendrá igual
serial = 'Q2LW-3D2D-LP5T'                                #<<<<<<<<<<<<<Cambiar variable del serial donde estan los svis              

# Ruta del archivo .txt que contiene la información
input_file = "C:/RootScripts/Appelt/MW/SVIsId.txt"     #<<<<<<<<<<<<<Cambiar variable del path
                
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
        
        # Extraer el nombre
        nombre = row['name']
        
        # Extraer el interface ID
        interface_id = row['interfaceId']
        
        # Crear la entrada del diccionario con 'interface_id_' seguido por el nombre
        sitios[clave] = {
            'nombre': nombre,
            'serial': serial,
            f"interface_id_{nombre}": interface_id
        }
        
        # Incrementar la letra para la siguiente clave
        clave_letra += 1

# Mostrar el diccionario resultante
print(sitios)
