"""
Escribir una función que reciba una lista de diccionarios, y que nos devuelva una lista con los valores únicos de los diccionarios.

ejemplo: ['Primero', 'Segundo', 'Tercero', 'Cuarto', 'Quinto']
"""

listD_ent = [{"A":"Primero"}, {"B": "Segundo"}, {"b":"Segundo"}, {"C":"Tercero"}, {"D": "Cuarto"}, {"d":"Cuarto"},{"E": "Quinto"}]

final = []

"""
for i in listD_ent:
    for j, k in i.items():
        if k not in final:
            final.append(k)
"""

for i in listD_ent:
    for j in i.keys():
        print(j)

    for k in i.values():
        print(k)
    for l in i.keys():
        print(i[l])
    
    #for m in i.keys():
        #if i[m] not in final:
            #final.append(i[m])
    
    for n in i.values():
        if n not in final:
            final.append(n)


print(final)

