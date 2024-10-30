# Dado un numero binario mayor a 3 digitos, contar las veces que tiene el patron 1 0 1, este patro debe seguir este orden y puede o no
# ser consecutivos ejemplo: 1 0 1 0 0 1 0

num = ['1', '0', '1', '0', '0', '1', '0']
patron = ["1", "0", "1"]


k = 0
j = k + 1
i = j + 1

cuenta = 0

for _ in num[k: len(num)+1]:
    K = num[k]
    for J in num[j:len(num)+1]:
        J = num[j]
        for I in num[j+1: len(num)+1]:
            I = num[i]
            if K=='1' and J == '0' and I == '1':
                cuenta += 1
            i += 1
        j += 1   
        i = j + 1 
    k += 1
    j = k + 1
    i = j + 1
print(cuenta)
    