"""
Escribir una función que reciba como parámetros, dos numeros que va a corresponder a los extremos del intervalo, es decir si recibe 2,10: vamos a trabajar en el intervalo [2,10]
La función nos debe generar un diccionario, donde las llaves son los números de nuestro intervalo y los valores van a ser el valor de llave -1.
Es decir si recibimos 2,4 el diccionario esperado va a ser : {2:1, 3:2, 4:3}
"""

dicc = {}

num = [int(a) for a in input().split()]

num.sort()
cont = 0
for i in range((num[-1]- num[0])+1):
    dicc[num[0] + cont] = (num[0] + cont) -1
    cont+=1

print(dicc)