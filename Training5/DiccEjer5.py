"""
Escribir una función que reciba una lista de diccionarios, y que nos devuelva una lista con los valores únicos de los diccionarios.

ejemplo: ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto']
"""

listD_ent = [{"A":"Primero"}, {"B": "Segundo"}, {"b":"Segundo"}, {"C":"Tercero"}, {"D": "Cuarto"}, {"d":"Cuarto"},{"E": "Quinto"}]

final = []

for i in listD_ent:
    for j in i:
        if i[j] not in final:
            final.append(i[j])


for i in listD_ent:
    for llaves, valores in i.items():
        if valores not in final:
            final.append(valores)


for i in listD_ent:
    for values in i.values():
        if values not in final:
            final.append(values)


for i in listD_ent:
    for keys in i.keys():
        if keys not in final:
            final.append(keys)            

print(final)
