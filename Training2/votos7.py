
partidos = {'pri': 0, 'pan': 0, 'morena':0}

resp = 'si'

while resp == 'si':
    voto = input("Por cual partido quieres votar? \n")
    if voto in partidos:
        partidos[voto] += 1
    else:
        partidos[voto] = 1
    resp = input("Quieres seguir votando? \n")

num = []

for i in partidos:
    num.append(partidos[i])
    
num.sort()

for indice, valor in partidos.items():
    if valor == num[-1]:
        print(indice)