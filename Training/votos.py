"""
Realizar un programa que cuente los votos de un partido y en caso de que una persona vote
por un partido que no este en la base de datos se el partido con un voto
"""
from pprint import pprint
partidos = {"pri": 0, "pan":0, "morena": 0}


resp = "si"
while resp == "si":
    voto = input("Que partido quieres votar:")
    if voto in partidos:
        partidos[voto]+=1
    else:
        partidos[voto] = 1
    print(partidos)     
    resp = input("Quieres seguir votando: \n")
cuenta = []
for i in partidos:
    cuenta.append(partidos[i])
cuenta.sort()

for indice, llave in partidos.items():
    if llave == cuenta[-1]:
        print(f"El partido ganador fue {indice} con {partidos[indice]} votos")
pprint(partidos)