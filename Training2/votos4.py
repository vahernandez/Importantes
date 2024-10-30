"""
Realizar un programa que cuente los votos de un partido y en caso de que una persona vote
por un partido que no este en la base de datos se el partido con un voto
"""

partidos = {'pri': 0, 'pan': 0, 'morena':0}

resp = 'si'

while resp == 'si':
    votos = input("Que partido quieres votar: ? \n")
    if votos in partidos:
        partidos[votos] += 1
    else:
        partidos[votos] = 1
    resp = input(' Quieres seguir votando? \n')
cont = []

for i in partidos:
    cont.append(i)
cont.sort()

for indice, llave in partidos.items():
    if llave == partidos[indice]:
        print( " El partido ganador es", llave)   
print(partidos) 
