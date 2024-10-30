"""
Función que crea y devuelve una lista con n números enteros con valores entre a y b
"""

limInf = 1  #limite inferior
limSup = 10  # limite superior

def crea (limInf, limSup):
    lista = []
    for i in range(limInf, limSup+1):
        lista.append(i)
    return lista

print(crea(limInf, limSup))


# Ahora con random

import random

def crear (n, a, b):  # la n es cuantos numero quiero en la lista, a y b los limites
    listas = []
    for i in range(n):
        listas.append(random.randint(a,b))
    return listas
print(crear(5, 1, 10))