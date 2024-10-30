"""
Tienes una matriz de 5x5 que consiste en 24 ceros y un solo número uno. Vamos a indexar las filas de la matriz con números del 1 al 5 de arriba hacia abajo, y vamos a 
indexar las columnas de la matriz con números del 1 al 5 de izquierda a derecha.

input:
0 0 0 0 0
0 0 0 0 1
0 0 0 0 0
0 0 0 0 0
0 0 0 0 0

output = 3
"""

filas = [input() for _ in range(5)] # se hace un lista preguntando 5 veces input

listas = {}   # Se crea un diccionario en blanco

for i in range(5):
    listas[f"lista{i + 1}"] = [int(a) for a in filas[i].split()] # Se llena el diccionario  osea listas[llave] = valor
#aqui se ve porque desde el principio se guarda los inputs en una lista ya que a travez de un LC le otorgamos un valor a cada llave
#
    
offsets = [2, 1, 0, 1, 2]

for n in range(5):
    lista = listas[f"lista{n + 1}"]
    for a in range(5):
        if lista[a] == 1:
            print(offsets[n] + abs(a - 2))
            break


#lista1, lista2, lista3, lista4, lista5 = [listas[f"lista{i + 1}"] for i in range(5)]

"""


for n in range(5):
    if n == 0:
        for a in range(5):
            if lista1[a] == 1:
                #lista1[a], lista3[2] = 0, 1
                print(2 + abs(a - 2))
                break
    elif n == 1:
        for a in range(5):
            if lista2[a] == 1:
                #lista2[a], lista3[2] = 0, 1
                print(1 + abs(a - 2))
                break
    elif n == 3:
        for a in range(5):
            if lista4[a] == 1:
                #lista4[a], lista3[2] = 0, 1
                print(1 + abs(a - 2))
                break
    elif n ==4:
        for a in range(5):
            if lista5[a] == 1:
                #lista5[a], lista3[2] = 0, 1
                print(2+ abs(a - 2))
                break
    elif n == 2:
        for a in range(5):
            if lista3[a] == 1:
                #lista3[a], lista3[2] = 0, 1
                print(abs(a - 2))
                break


"""


