"""
Escribir una función que reciba una lista de diccionarios, y que nos devuelva una lista con los valores únicos de los diccionarios.

ejemplo: ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto']
"""

listD_ent = [{"A":"Primero"}, {"B": "Segundo"}, {"b":"Segundo"}, {"C":"Tercero"}, {"D": "Cuarto"}, {"d":"Cuarto"},{"E": "Quinto"}]


def foo (lista):
    listaF = []
    for elemento in lista:
        for llave in elemento.keys():
            if elemento[llave] not in listaF:
                listaF.append(elemento[llave])
    return listaF



print(foo(listD_ent))