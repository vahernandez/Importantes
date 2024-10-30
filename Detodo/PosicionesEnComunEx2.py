# Leer dos arreglos, imprimir todas las posiciones donde dos datos en ambos arreglos son iguales ejemp
# [1 5 3 8]
# [4 5 2 8]
# respuesta: [1 3]

repetidos = []

uno = ['1', '5', '5', '8']
dos = ['4', '5', '4', '8']
posI = 0
posJ = 0
for i in uno:
    for j in dos:
        if j == i and posI == posJ:
            repetidos.append(i)
            break
        else:
            posI += 1
    posJ += 1
    posI = 0
print(repetidos)