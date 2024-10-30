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

Vizq = 0
Vder = 8
dist= 0
resp = []
x= 1
for i in alturas[Vizq:Vder]:
    print(Vizq, Vder)
    dist = len(alturas) - x
    print(len(alturas))
    if Vder>Vizq:
        resp.append(alturas[Vizq] * dist)
    else:
        resp.append(Vder * dist)
    x+=1
        
print(resp)

