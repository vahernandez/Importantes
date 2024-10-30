import csv

# Nombre del archivo CSV de entrada y salida
input_csv =  r'C:/Users/vhernandezl/OneDrive - New Process Steel/Documents/NPS/Scripts/CGScripts/entrada.csv'
output_csv = r'C:/Users/vhernandezl/OneDrive - New Process Steel/Documents/NPS/Scripts/CGScripts/salida.csv'

# Abrir el archivo CSV de entrada y crear el archivo CSV de salida
with open(input_csv, 'r') as csv_file, open(output_csv, 'w', newline='') as output_file:
    reader = csv.reader(csv_file)
    writer = csv.writer(output_file)

    for row in reader:
        try:
            # Leer los valores de las dos primeras columnas y calcular la suma
            num1 = int(row[0])
            num2 = int(row[1])
            suma = num1 + num2
            
            # Agregar la suma como tercer columna
            row.append(suma)
            writer.writerow(row)
        except (ValueError, IndexError):
            print(f"Error en la fila: {row}")

print("Proceso completado. Se ha generado el archivo de salida:", output_csv)

