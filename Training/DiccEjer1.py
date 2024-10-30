"""
Escribir una función que reciba una lista de diccionarios, y que nos devuelva una lista con los valores únicos de los diccionarios.

ejemplo: ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto']
"""

listD_ent = [{"A":"Primero"}, {"B": "Segundo"}, {"b":"Segundo"}, {"C":"Tercero"}, {"D": "Cuarto"}, {"d":"Cuarto"},{"E": "Quinto"}]

def foo (lista):   
    listaF = []  # lista final vacía
    for elemento in lista:  # Se itera sobre la lista de diccionarios y extraemos cada uno de los elementos de esta lista y lo guardamos en la variable "elemento".
        for llave in list(elemento.keys()):  # Al analizar la variable "elemento" , creamos la variable "llave" (del for) y con list(elemento.keys()) extraemos el VALOR del diccionario que se analiza y lo guardamos en "llave"
            if elemento[llave] not in listaF:  # ahora usamos las dos variables "elemento" y "llave" donde el elemento si elemento[llave] o lo que es lo mismo SI "Primero" no esta en la listaF, agregalo
                listaF.append(elemento[llave])
    return listaF

print(foo(listD_ent))