import random

# Lista original
listaI = [2, 5001, 5]

# Inicializar la lista que se ordenará
lista = listaI

# Pila para almacenar las sublistas que se van a ordenar
pila = [lista]

# Lista final que contendrá la lista ordenada
listaOrdenada = []

# Ejecutar el algoritmo mientras haya sublistas en la pila
while pila:
    # Tomar la sublista actual
    lista = pila.pop()

    # Si la sublista tiene un solo elemento o está vacía, añadirla a la lista ordenada
    if len(lista) <= 1:
        listaOrdenada.extend(lista)
    else:
        # Seleccionar un pivote al azar
        pivote = random.choice(lista)

        # Dividir la lista en tres partes: menores, iguales y mayores
        menores = [x for x in lista if x < pivote]
        iguales = [x for x in lista if x == pivote]
        mayores = [x for x in lista if x > pivote]

        # Añadir las sublistas a la pila para ordenarlas
        pila.append(mayores)
        pila.append(iguales)
        pila.append(menores)

# Mostrar la lista original y la lista ordenada
print("Lista original:", listaI)
print("Lista ordenada:", listaOrdenada)