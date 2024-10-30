"""
Haz una función que devuelva la distacia entre dos puntos
"""

import math

def distancia (a,b):
    distX = a[0] - b[0]    # Calculo de un cateto
    distY = a[1] - b[1]    # Calculo del otro cateto
    distTotal = math.sqrt(distX**2 + distY**2)  # Pitagoras
    return distTotal
print(distancia([5,7],[3,2]))  # Los inputs se dan con dos listas, en cada lista tiene que ser de la forma x1, y1 y x2, y2