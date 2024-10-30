"""
Una permutación es una disposición ordenada de objetos. Por ejemplo, 3124 es una posible permutación de los 
digitos 1, 2, 3 y 4. Si todas las permutaciones se enumeran numéricamente o alfabéticamente, lo llamamos
orden lixicográfico. Las permutaciones lixicográficas de 0,1 y 2 son:
012 021 102 120 201 210
¿Cual es la millonésima permutación lexicográfica de los digítos 0, 1, 2, 3, 4, 5, 6, 7, 8 y 9?
"""

base = [0 , 1]
perm = []
izq = 0
der = -1
dicc = {}
cont = 0
for i in list(range(2)):
    base[0]= izq
    base[-1]= i
    dicc[i]=(base)
    cont+=1
    print(base)
    print(dicc)
    
    
    
    
    
    
cccccbifdjuvilcdncbjgkighreruftuvjujttcduhjj


