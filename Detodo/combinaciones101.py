# Dado un numero binario mayor a 3 digitos, contar las veces que tiene el patron 1 0 1, este patro debe seguir este orden y puede o no
# ser consecutivos ejemplo: 1 0 1 0 0 1 0
# 

num = ['1', '0', '1', '0', '0', '1', '0']

long = len(num)

cuenta = 0

J = 1
K = 0
for k in (num[K: -1]):
    for j in (num[K+J: -1] ):
        for i in num[1+(K+J):-1]:
            if k == '1' and j == '0' and i == '1':
                cuenta += 1
            else:
                pass
        J += 1
    K += 1
    J = 1
print (cuenta)
        
