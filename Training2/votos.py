"""
Realizar un programa que cuente los votos de un partido y en caso de que una persona vote
por un partido que no este en la base de datos se el partido con un voto
"""

partidos = {'pri': 0, 'pan': 0, 'morena':0}

res = 'si'
while res =='si':
    
    voto = input("Que partido quieres vota? \n")

    if voto in partidos:
        partidos[voto]+=1
    else:
        partidos[voto]=1
    print(partidos)
    res = input("Quieres seguir votando? \n")

cont = []
for i in partidos:
    cont.append(partidos[-1])
cont.sort()

for indice, llave in partidos.items():
    if llave == cont[-1]:
        print(f"El partido ganador es {indice}")
    
