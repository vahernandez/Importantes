
dicc = {}
resp = 'si'

while resp == 'si':
    votos = input("Por que partido quiere votar? \n")
    if votos in dicc:
        dicc[votos] += 1
    else:
        dicc[votos] = 1
    resp = input("Quieres seguir votando? \n")

cuenta = []

for i in dicc:
    cuenta.append(dicc[i])

cuenta.sort()

for i, j in dicc.items():
    if cuenta[-1] == j:
        print("El partido", i, "es el partido ganador con", j, "votos") 
