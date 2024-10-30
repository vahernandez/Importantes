# ser consecutivos ejemplo: 1 0 1 0 0 1 0
# 

num = ['1', '0', '1', '0', '0', '1', '0']

contador = 0
K=0
J=1

for k in num[K:-1]:
    for j in num[J+K: -1]:
        for i in num[(1+J+K) : -1]:
            if k== '1' and j == '0' and i == '1':
                contador += 1
            else:
                pass
        J += 1
    J = 1    # Es necesario resetear J a su valor inicial de 1 para que no conserve los valores que tomo durante el ciclo for
    K += 1
print(contador)    