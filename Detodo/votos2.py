"""
Crear un programa que cuente los votos de un partido político y en caso de que el votante vote por un partido político que no este en la boleta crear este 
partido que no esta registrado en la boleta con un valor de uno. Al final debe de mostrar cual fue el partido ganador.
"""

baseDatos = {"pri":0, "pan": 0, "morena":0}
respuesta = "si"
while respuesta == "si":
    voto = input("Por cual partido político quieres votar? \n")
    if voto in baseDatos:
        baseDatos[voto]+=1
    else:
        baseDatos[voto] = 1
    respuesta = input("Hay otra persona que va a votar despues de ti? \n")
print(baseDatos)

cuenta = []

for i in baseDatos:
    cuenta.append(baseDatos[i])

cuenta.sort()
valorBuscado = cuenta[-1]
for indice, valor in baseDatos.items():
    if valorBuscado == valor:
        print("El partido que ganó fué: ", indice)

