"""
Se te da un arreglo de enteros height de longitud n. Hay n líneas verticales dibujadas de tal manera que los dos extremos de la línea i-ésima son (i, 0) y (i, height[i]).
Encuentra dos líneas que, junto con el eje x, formen un contenedor, de manera que el contenedor contenga la mayor cantidad de agua posible.
Devuelve la cantidad máxima de agua que un contenedor puede almacenar.
Nota que no puedes inclinar el contenedor.
Input: height = [1,8,6,2,5,4,8,3,7]

8  |      @@                       @@                                     
7  |      @@                       @@        @@                            
6  |      @@   @@                  @@        @@                             
5  |      @@   @@        @@        @@        @@                              
4  |      @@   @@        @@   @@   @@        @@                             
3  |      @@   @@        @@   @@   @@   @@   @@                                  
2  |      @@   @@   @@   @@   @@   @@   @@   @@                                  
1  | @@   @@   @@   @@   @@   @@   @@   @@   @@                       
   ------------------------------------------------>
     1    2    3    4    5    6    7    8    9         
                                                                            
"""
from pprint import pprint
alturas = [1,8,6,2,5,4,8,3,7]

area = []
dicc = {}
left = 0
der = 8
cont = 0
while left != der:
    #print(left, der)
    for i in alturas[left:der]:
        dicc[left, der] = (alturas[der], alturas[left])
        #print(dicc)
        #print(alturas[der], alturas[left])
        if alturas[left]< alturas[der]:
            area.append(alturas[left] * (der-left))
            der = der -1
        else:
            area.append(alturas[der] * (der - left))
            left = left +1   
    cont += 1
    left = cont
    der = 8
area.sort()

print(area[-1])
#print(dicc)