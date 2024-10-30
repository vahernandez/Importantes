"""
Realizar un programa que cuente los votos de un partido y en caso de que una persona vote
por un partido que no este en la base de datos se el partido con un voto
"""

voto = {}
resp = 'si'
while resp == 'si':
    partido = input("¿Por cual partido quieres votar: ? \n")
    if partido not in voto:
        voto[partido] = 1
        print (voto)
        resp = input("Quieres seguir votando?")
    else:
        voto[partido] += 1
        print(voto)
        resp = input("Quieres seguir votando?")
print(voto)

cuenta = []

for i in voto:
    cuenta.append(voto[i])
cuenta.sort()
print (cuenta)
for indice, llave in voto.items():
    if llave == cuenta[-1]:
        print(indice)

