"""
Realizar un programa que cuente los votos de un partido y en caso de que una persona vote
por un partido que no este en la base de datos se el partido con un voto
"""

partidos = {'pri': 0, 'pan': 0, 'morena':0}

res = "si"
while res == "si":
    voto = input("Porque partido quieres votar?: \n")
    if voto in partidos:
        partidos[voto]+=1 
    else:
        partidos[voto] = 1
    res = input("Quieres seguir votando? \n")
print(partidos)

cuenta = []

for i in partidos:
    cuenta.append(partidos[i])
cuenta.sort()

for indice, llave in partidos.items():
    if llave == cuenta[-1]:
        print(f'El ganador es indice {indice}')
print(cuenta)