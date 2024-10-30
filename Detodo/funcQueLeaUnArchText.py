"""
Crea una función que lea los renglones de un archivo de texto
"""

with open ("C:\inputs\leer.txt", "r") as archivo: # with open para abrir el archivo y r es modo lectura y lo guardo en un archivo llamado archivo
    datos = archivo.readlines()  #  a archivo le aplico un metodo el cual lee los renglones y lo guarda en otra variable llamada datos

for i in datos:   # iteramos datos
    i = i.replace("\n", "")  # reemplazamos los saltos de linea por nada
    print(i)


# archivo es el nombre que le quiero dar a mi variable para acceder el archivo leer.txt

# Basicamente lo podemos entender sin decir que es asi exactamente pero para propositos de entendimiento que :
# Abrimos un archivo en modo lectura
# Lo guardamos en una variable que nos sirve para mi cache
# Creamos otra variable en el cual se guarda el resultado del proceso hecho a la primer variable en este caso el proceso hecho fue leer por renglon
# iteramos sobre el segundo archivo creado y en cada iteración hacemos print para ver el contenido por renglon





