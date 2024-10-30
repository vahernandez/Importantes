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
def capturar ():
    global lista
    lista = []
    n = int(input("Cuantos elementos va a tener la lista? "))
    for i in range (0, n):
        elem = int(input("Ingresa el Elemento del Indice: "))
        lista.insert(i,elem)
capturar()

# Definiendo la función a mostrar
def mostrar():
    print(lista)
mostrar()

#    

