"""
Realizar un programa que cuente los votos de un partido y en caso de que una persona vote
por un partido que no este en la base de datos se el partido con un voto
"""

partidos = {'pri': 0, 'pan': 0, 'morena':0}

def foo (partidos):
    resp = 'si'
    while resp == 'si':
        voto = input("Que partido quieres votar? \n")
        if voto in partidos:
            partidos[voto] += 1
        else:
            partidos[voto] = 1
        resp = input("Quieres seguir votando")

    cantidad = []

    for i in partidos:
        cantidad.append(partidos[i]) 
        
    cantidad.sort()

    for indice, valor in partidos.items():
        if cantidad[-1] == valor:
            return indice, partidos

print(foo(partidos))