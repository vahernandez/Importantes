partidos = {'pri': 0, 'pan': 0, 'morena':0}

resp = 'si'

while resp == 'si':
    voto = input( " Porque partido quieres votar? \n")
    if voto in partidos:
        partidos[voto] += 1
    else:
        partidos[voto] == 1
    
    resp = input("Quieres seguir votando? \n")
    
cuenta = []
    
for i in partidos:
    cuenta.append(partidos[i])

cuenta.sort()

for indice, valor in partidos.items():
    if valor == cuenta[-1]:
        print(indice)

    