import csv

gen_csv = 'nuevo.csv'

# Crear y abrir el archivo CSV en modo de escritura
with open(gen_csv, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    
    # Escribir "hola" en la primera columna cuatro veces
    for i in range(4):
        writer.writerow(["hola"])

print("Archivo CSV generado:", gen_csv)