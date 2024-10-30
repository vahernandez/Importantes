"""
Bob se está preparando para pasar un test de CI. La tarea más frecuente en este test es averiguar cuál de los n números dados es diferente de los demás. Bob observó que un número 
generalmente difiere de los otros en si un número es par o impar. Ayuda a Bob: para comprobar sus respuestas, necesita un programa que, entre los n números dados, encuentre uno que 
sea diferente en si un número es par o impar.

Entrada
La primera línea contiene un número entero n (3 ≤ n ≤ 100) — la cantidad de números en la tarea. La segunda línea contiene n números naturales separados por espacios, no excediendo 100. 
Se garantiza que exactamente uno de estos números difiere de los demás en si un número es par o impar.

Salida
Imprime el índice del número que difiere de los demás en si un número es par o impar. Los números están numerados desde 1 en el orden de entrada.
"""

cant = int(input())
lista = [int(a) for a in input().split()]
"""
count1 = 0
count2 = 0
dicc2 = {}
dicc1 = {}
count = 0

for i in lista:
    if i%2 ==0:
        dicc1[count] = i
        count1 += 1
    else:
        dicc2[count] = i
        count2 += 1
    count += 1
    if count == len(lista):
        if count1>1:
            print([int(a) for a in dicc2][0])
        else:
            print([int(a) for a in dicc1][0])
"""


#######################################

pares = [a for a in lista if a%2 ==0]  # encontrar los pares 
impares = [a for a in lista if a%2 != 0]  # y los impares y colocarlos en listas

if len(pares) > 1:  # ver cual tiene solo un elemento en la lista
    print(lista.index(impares[0])+1)  # a ese que tiene solo un elemento vemos que indice le corresponde
else:
    print(lista.index(pares[0])+1)   # de la lista original y se imprime
