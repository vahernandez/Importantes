"""
Imprime YES si el número de dígitos de la suerte( 4 o 7) en él es un número de la suerte (7)

por ejemplo 4, 7, 0, 0, 0, 7, 7, 4, 7, 0, 4, si es un nearlyLuckynumber porque los dígitos 4, o 7 dan una suma de 7 o 4.

"""

num= [int(a) for a in input()]

filter = []

for i in num:
    if i == 4 or i == 7:
        filter.append(i)
if len(filter) == 7:
    print("YES")
elif len(filter) == 4:
    print("YES")
else:
    print("NO")
    

    