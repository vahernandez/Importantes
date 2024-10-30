# Realizar un programa que cuente los votos de un partido y en caso de que no una persona vote por un partido que no este en la base datos
# se crea el partido con un voto.

dicc = {}
voto = input( " Teclea el partido por el cual quieras votar, en caso de que quieras terminar teclea no: \n")
while voto != 'no' :
    if voto in dicc:
        dicc[voto] += 1
    else:
        dicc[voto] = 1
    voto = input( " Teclea el partido por el cual quieras votar,  en caso de que quieras terminar teclea no:: \n")
print(dicc)


"""
for i in dicc:
    voto = input( " Teclea el partido por el cual quieras votar: \n")
    if voto in dicc:
        dicc[voto] += 1
    else:
        dicc[voto] = 1
print(dicc)
"""
