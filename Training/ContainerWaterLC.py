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
volumen = 0
resultado = []
altura = 0
ejeIzq = 0

for j in alturas[ejeIzq: len(alturas)+1]:
    incremento = 0
    ejeDer= ejeIzq + 1
    for i in alturas[ejeIzq:-1]:
        orden = [alturas[ejeIzq], alturas[ejeDer]]
        orden.sort()
        volumen = orden[0] * (incremento + 1)
        incremento+=1
        resultado.append(volumen)
        ejeDer += 1
    ejeIzq += 1
resultado.sort()
print(resultado[-1])
    


    
    
