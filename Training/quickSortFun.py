import random

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = random.choice(lista)
        menores = [x for x in lista if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista if x > pivote]
        return quicksort(menores) + iguales + quicksort(mayores)

listaI = [2, 5001, 5]

print("Lista original:", listaI)
listaOrdenada = quicksort(listaI)
print("Lista ordenada:", listaOrdenada)