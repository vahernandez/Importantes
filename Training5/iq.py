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


num = int(input())
lista = [int(a) for a in input(" ").split()]
dicc = {}    # se va guardar la información en un diccionario
k=1
par = 0
impar = 0
for i in lista:  # la intencion es convertir los pares en 0s y los impares en 1s
    if i % 2 ==0:
        dicc[k]=0  # la llave del diccionario indicará el orden de todos los numeros
        par+=1
    else:
        dicc[k]=1
        impar+=1
    k+=1
if par > impar:  # Debido a que solo hay un UNO o un CERO podemos usar un if 
    for i, j in dicc.items():    # adentro de este if vamos a usar un for para detectar el numero diferente
        if j == 1:               # una vez detectado el numero diferente vemos que 
            print(i)             # que llave tiene el cual indica el orden de la lista y la respuesta
else:
    for i, j in dicc.items():
        if j == 0:
            print(i)


    

