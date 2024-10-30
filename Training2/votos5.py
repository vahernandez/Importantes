"""
Realizar un programa que cuente los votos de un partido y en caso de que una persona vote
por un partido que no este en la base de datos se el partido con un voto
"""

partidos = {'pri': 0, 'pan': 0, 'morena':0}

resp = 'si'
while resp == 'si':
    voto = input(" Por que partido vas a votar: \n")
    if voto in partidos:
        partidos[voto] += 1
    else:
        partidos[voto] = 1
    resp = input("Quieres seguir votando? \n")

cantidad = []
for i in partidos:
    cantidad.append(partidos[i])

cantidad.sort()

for indice, valor in partidos.items():
    if cantidad[-1] == valor:
        print(indice)
print(partidos)
