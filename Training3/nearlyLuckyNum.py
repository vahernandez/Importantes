"""
Imprime YES si el número de dígitos de la suerte( 4 o 7) en él es un número de la suerte (7)

por ejemplo 4, 7, 0, 0, 0, 7, 7, 4, 7, 0, 4, si es un nearlyLuckynumber porque los dígitos 4, o 7 dan una suma de 7 o 4.

"""

numero = [int(a) for a in input()]
cont = 1
cuatros = []
for i in numero:
    if i == 4 or i == 7:
        cuatros.append(i)
    if cont == len(numero):
        if len(cuatros) == 4 or len(cuatros) == 7:
            print("YES")
        else:
            print("NO")  
    cont+=1
    

# 4700007747047