partidos = {'pri': 0, 'pan': 0, 'morena':0}

resp = 'si'

while resp == 'si':
    voto = input("Porque partido quieres votar: ? \n")
    if voto in partidos:
        partidos[voto] += 1
    else:
        partidos[voto] = 1
    resp = input("quieres sguir votando? \n")

cuenta = [int(partidos[i]) for i in partidos]

cuenta.sort()

for indice, llave in partidos.items():
    if cuenta[-1] == llave:
        print(f'El partido ganador es {indice}')