"""
Imprime YES si el número de dígitos de la suerte( 4 o 7) en él es un número de la suerte (7)

por ejemplo 4, 7, 0, 0, 0, 7, 7, 4, 7, 0, 4, si es un nearlyLuckynumber porque los dígitos 4, o 7 dan una suma de 7.

"""
numero = [int(a) for a in input()]
cont = []
cuenta = 0
for i in numero:
    if i == 4 or i == 7:
        cont.append(i)
        cuenta += 1
    else:
        cont.append(1)
if 4 in cont and 7 in cont and 1 not in cont:
    print('YES')
elif cuenta == 4 or cuenta == 7:
    print('YES')
else:
    print('NO')


