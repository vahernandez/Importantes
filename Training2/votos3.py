"""
Realizar un programa que cuente los votos de un partido y en caso de que una persona vote
por un partido que no este en la base de datos se el partido con un voto
"""

partidos = {'pri': 0, 'pan': 0, 'morena':0}

resp = 'si'

while resp == 'si':
    voto = input("Por cual candidato vas a votar? \n")
    if voto in partidos:
        partidos[voto] +=1
    else:
        partidos[voto] = 1
    resp = input("Quieres seguir votando? \n")
cuenta = []
for i in partidos:
    cuenta.append(partidos[i])
cuenta.sort()
print(cuenta)

for indice, llave in partidos.items():
    if llave == cuenta[-1]:
        print(f"El ganador es {indice}")
print(partidos)