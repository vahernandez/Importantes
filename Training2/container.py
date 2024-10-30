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

alturas = [1,8,6,2,5,4,8,3,7]
area = []
izq = 0
a = 1

for i in alturas[izq : len(alturas)+1]:
    der = (len(alturas))-a
    for j in alturas[izq:der]:
        der = (len(alturas))-a
        if alturas[izq]<= alturas[der]:
            area.append(alturas[izq] * (der-izq))
        else:
            area.append(alturas[der] * (der - izq) )
        a+=1
    a=1
    izq += 1
area.sort()

print(area[-1])