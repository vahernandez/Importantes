# Dado un numero binario mayor a 3 digitos, contar las veces que tiene el patron 1 0 1, este patro debe seguir este orden y puede o no
# ser consecutivos ejemplo: 1 0 1 0 0 1 0

num = ['1', '0', '1', '0', '0', '1', '0']
patron = ["1", "0", "1"]

Primero = 0   # subindices
Segundo= 1
cuenta = 0
long = len(num)

for k in num[Primero:(len(num)+1)]:
    for j in num[Primero+Segundo: (len(num)+1)]:
        for i in num[1+(Primero+Segundo): (len(num)+1)]:   #subindices
            if k == '1' and j == '0' and i == "1":
                cuenta+=1
            else:
                pass
        Segundo+=1
    Segundo=0
    Primero+=1
print(cuenta)



