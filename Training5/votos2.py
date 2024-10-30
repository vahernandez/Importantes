voto = {}

resp = 'si'

while resp == 'si':
    palabra = input("Por cual partido político te gustaría votar? \n")
    if palabra in voto:
        voto[palabra]+=1
        resp = input("Quieres seguir votando? \n")
    else:
        voto[palabra] = 1
        resp = input("Quieres seguir votando ? \n")
    
print(voto)

cuenta = []

for i in voto:
    cuenta.append(voto[i])

print(cuenta)

for indice, llave in voto.items():
    if llave == cuenta[-1]:
        print(indice)