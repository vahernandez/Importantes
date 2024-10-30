import csv
import os
"""
# Nombre del archivo CSV de entrada y salida
input_csv =  r'C:/Users/vhernandezl/OneDrive - New Process Steel/Documents/NPS/Scripts/CGScripts/entrada.csv'
output_csv = r'C:/Users/vhernandezl/OneDrive - New Process Steel/Documents/NPS/Scripts/CGScripts/salida.csv'



# Abrir el archivo CSV de entrada y crear el archivo CSV de salida
with open(input_csv, 'r') as csv_file:
    reader = csv.reader(csv_file)

    for row in reader:
        try:
            # Leer los valores de las dos primeras columnas y calcular la suma
            num1 = float(row[0])
            num2 = float(row[1])
            suma = num1 + num2
            
            # Agregar la suma como tercer columna
            print(suma)
        except (ValueError, IndexError):
            print(f"Error en la fila: {row}")

print("Proceso completado.")


with open(input_csv, 'r') as csv_file, open(output_csv, 'w', newline='') as output_file:  
                                        # with sirve para manejar operaciones de abrir y cerrar archivos, open abre una variable la cual previamente apuntaba a un archivo, esa variable se convierte en otra variable 
                                        #sobre la cual va a recaer el procesamiento o tratamiento que se requiera hacer por ejemplo en este codigo ocupamos leer dos valores de dos diferentes columnas por eso hicimos
                                        # otra variable, en la nueva variable podemos separar los valores por comma y poder procersarlos
    reader = csv.reader(csv_file)       # Ya que tenemos la variable lista para ser procesada por funciones de excel le aplicamos una funcion que se llama reader y crea otro objeto llamada reader que se utilizara en el for
    writer = csv.writer(output_file)
    for linea in reader:
        num1 = int(linea[0])
        num2 = int(linea[1])
        suma = num1 + num2
        linea.append(suma)
        writer.writerow(linea)
        
print("Proceso completado. Se ha generado el archivo de salida:", output_csv)



"""



output_csv1 = r'C:/Users/vhernandezl/OneDrive - New Process Steel/Documents/NPS/Scripts/CGScripts/salida11.csv'

with open(output_csv1, 'w', newline='') as output_file1:
    writer = csv.writer(output_file1)
    
    for _ in range(4):
        num1 = int(input("Ingresa un número: "))
        linea = [num1]
        linea.append("hola")
        writer.writerow(linea)

print("Proceso completado. Se ha generado el archivo de salida:", output_csv1)
