from funciones import *
"""Escribir un programa que permita procesar datos de subscriptores de una tienda en linea en una lista de tuplas con el siguiente formato:
[(ale86, 040286, Standard), (vale79, 110579, Gold), (leon14, 271114, Platinum)]
Ademas, en otra lista de tuplas se almacenan los el tope de cada nivel de subscripción:
[(Standard, 5k), (Gold, 10k), (Platinum, 20k)]
Hacer un menú interactivo que permita al usuario realizar las siguientes operaciones:
1. Agregar subscriptores a la lista de subscriptores.
2. Agregar los niveles de subscrición con su linea de credito correspondiente
3. Dado un id de un usuario buscar a que nivel de subscrición pertenece.
4. Dado un nivel de subscripción revisar cuantos usuarios pertenecen a ese nivel.
5. Dada un id de un subscriptor mostrar cual es su linea de credito.
6. Dada una linea de credito, mostrar cuantos subscriptores tienen ese beneficio.
7. Salir del programa. """

suscriptores = []
planes = []

while True:
    print("1. Agregar nuevo suscriptor: ")
    print("2. Agregar nuevo plan")
    print("Consultar que plan tienen un suscriptor")
    print("4. Consultar cuantos usuarios pertenecen a una subscripción dada")
    print("5. Consultar cual es la linea de credito dado un id de un suscriptor")
    print("6. Mostrar cuantos subscriptores pertenecen a una dada linea de credito")
    print("7. Salir del programa")
    print(" Menú : \n")
    opcion = int(input("Elige una opción: \n"))
    
    if opcion == 1:
        print("Agregar un subscriptor: \n")
        creaSuscriptores(suscriptores)
        print("Esta es la lista de suscriptores: ", suscriptores)
    
    elif opcion == 2:
        print("Agrega los planes de subscripción: ")
        creaPlanes(planes)
        print("Estos son los planes de subscripción: ", planes)
    else:
        print("Oción no válida")
        break