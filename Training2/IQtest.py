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

cantidad = int(input())
num = [int(a) for a in input(" ").split()]

indice = 1
par = []
impar = []
i = 0

for c in num:
    if c%2 ==0:
        par.append(c)
    else:
        impar.append(c)
minoria = 0
if len(par)<len(impar):
    minoria='pare'
else:
    minoria='impare'  

for b in range(len(num)-1):
    if (num[i] + num[i+1])%2 == 0:
        pass
    else:  # si el if se va para este else quiere decir que hay un cambio de par a impar o viceversa
        if minoria == 'pare':  # el numero par es el que estamos buscando o mas bien su indice
            if num[i]%2==0:  # Si dentro del par de numeros que se esta analizando, el primero de ellos es par
                print(indice)  # entonces imprimimos el indice de este numero ya que es el que estamos buscando
                break  # importante el break para que solo exista una respuesta de cambio osea el primer cambio 
            else: # entonces si el primer numero no es par quiere decir que el segundo numero del par de numeros 
                print(indice+1) # es el numero par osea el numero que estamos buscando, es por eso que le agregamos 1
                break
        else: # el numero impar es el estamos buscando o mas bien su indice
            if num[i]%2==0:  # Si dentro del par de numeros que se esta analizando, el primero de ellos es imppar
                print(indice+1)  # se le agrega un uno al indice
                break
            else: # dado que no el primer numero del par que se esta analizando no es par entonces por logica el primer numero
                print(indice)  
                break                 
    indice += 1
    i += 1
    
    """
         pare		      |            impare	
par_a_impar	 impar_a_par  |	 par_a_impar   impar_a_par
[2, 1]	       [1, 2]	  |     [2, 1]	    [1, 2]
indice	     indice +1	  |    indice+1	    indice

    """