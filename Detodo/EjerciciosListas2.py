# Ejercicio Práctico con Listas
"""
Manipulación de una Lista.
1. Capturar Lista
2. Mostrar Lista
3. Agregar un Elemento a la lista
4. Eliminar un Elemento de la lista
5. Modificar un Elemento de la lista
6. Salir
"""
# Definiendo la función a capturar


lista = []
n = int(input("Cuantos elementos va a tener la lista? \n"))
for i in range (0, n):
    print("Ingresa el Elemento del Indice", i, ": ")
    elem = int(input()) # los input en un for es para ir agregando los valores uno por uno
    lista.insert(i,elem)      # i va a estar iterando desde 0 hasta un numero entero de uno en uno, a lado va a tener el valor del indice

print(lista)

elem = int(input("Que elemento quieres agregar? \n"))
indice = int(input("Ingrese el índice donde desea Agregarlo? \n"))
longitud = int(len(lista))
if (indice > longitud or indice < 0):
    print ("El indice dbe estar entre 0 y ", longitud)
else:
    lista.insert(indice,elem)
    print("Elemento agregado")
print(lista)

print("s")

indice = int(input("Ingrese el índice del elemento que desea eliminar \n"))
longitud = int(len(lista))
if (indice > longitud or indice < 0):
    print("El indice debe estar entre 0 y ", longitud-1)
else:
    del lista[indice]
    print ("Elemento Eliminado")
print(lista)

indice = int(input("Ingrese el índice del elemento que desea modificar \n"))
elem = int(input("Que elemento quieres modificar? \n"))
longitud = int(len(lista))
if (indice > longitud or indice < 0):
    print("El indice debe estar entre 0 y ", longitud-1)
else:
    lista[indice] = elem
    print ("Elemento", indice, "Modificado")
print(lista)