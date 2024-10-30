"""
Escribir una función que reciba una lista de diccionarios, y que nos devuelva una lista con los valores únicos de los diccionarios.

ejemplo: ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto']
"""

listD_ent = [{"A":"Primero"}, {"B": "Segundo"}, {"b":"Segundo"}, {"C":"Tercero"}, {"D": "Cuarto"}, {"d":"Cuarto"},{"E": "Quinto"}]

final = []
"""
for item in listD_ent:
    for key, value in item.items():
        if value not in final:
            final.append(value)
"""




for i in listD_ent:
    for j in i.keys():
        if i[j] not in final:
            final.append(i[j])

print(final)