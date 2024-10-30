"""
Escribir una función que reciba una lista de diccionarios, y que nos devuelva una lista con los valores únicos de los diccionarios.

ejemplo: ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto']
"""

listD_ent = [{"A":"Primero"}, {"B": "Segundo"}, {"b":"Segundo"}, {"C":"Tercero"}, {"D": "Cuarto"}, {"d":"Cuarto"},{"E": "Quinto"}]

lista = []

for i in listD_ent:
    for j in i:
        if i[j] not in lista:
            lista.append(i[j])
print(lista)

print("**************************")

lista1 = []

for k in listD_ent:
    for m in k.values():
        if m not in lista1:
            lista1.append(m)
print(lista1)

print("**************************")

print(type(listD_ent))

[print(type(o)) for o in listD_ent[0:1]]