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

cuantos = int(input("Cuantos numeros se analizaran: \n"))
numeros = [int(a) for a in input("Teclea los numeros que se van analizar, recuerda que solo uno debe ser par/impar y el resto de los numeros lo opuesto: \n")]

pares = []
impares = []
for i in numeros:
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
if len(pares)==1:
    print(numeros.index(pares[0]))
else:
    print(numeros.index(impares[0]))
