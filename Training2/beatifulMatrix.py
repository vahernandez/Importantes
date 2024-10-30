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

listas = [input() for _ in range(5)] # las entradas seran tipo str y no podemos usar int(input())
dicc = {}

for i in range(5):
    dicc[f'lista{i+1}'] = [int(a) for a in listas[i].split()] # al usar esta LC vamos haciendo int cada numero

offset = [2,1,0,1,2]

cont = 0
ext = 0
for u in dicc:
    if 1 in dicc[u]:
        for e in dicc[u]:
            if e == 1:
                print(offset[ext] + abs(2 -cont))
            cont+=1
    ext+=1
    cont = 0  

  