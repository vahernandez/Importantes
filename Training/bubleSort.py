#import numpy as np

import random

listaI=[2,5001,5,5,2,5,8,7,200,199,100,88,77,3000,2501,1001]

#listaI=[2,5001,1,78,90]

def MenorMayor(lista):
    l=len(lista)  
    pivote = random.choice(lista)  # Se obtiene un numero al azar
    print (pivote)
    listNuevaSinPivote=[]  # Creamos un lista que no tenga el pivote
    count=0
    for i in range(l):     # Con este for creamos la lista sin el pivote
        if count >0:
            listNuevaSinPivote.append(lista[i])
        else:    
            if lista[i]!= pivote:
                listNuevaSinPivote.append(lista[i])
            else:
                count=count+1
    print(listNuevaSinPivote)

    listaBuffer=[]        # Esta lista nos servira para guardar una lista temporal
    n=0                   # Inicializamos las variables que vamos a necesitar
    x=0
    z=0
    listaFinal=[]         # Creamos la lista final
    for k in range(l-1):  # Hacemos un loop de l-1 veces
        listaBuffer.append(pivote)       # El primer número que ponemos en la lista temporal es el pivote
        for a in range(l-1):         # Con el for anidado comparamos el pivote con los numeros de
            if pivote < listNuevaSinPivote[n]:   # la lista que no tiene el pivote
                x=listNuevaSinPivote[n]
                n=n+1
                listaBuffer.append(x)          # Los acomodamos en la lista temporal
            else:
                x=listNuevaSinPivote[n]
                listaBuffer.insert(z, x)
                z=z+1
                n=n+1
        listNuevaSinPivote=[]          # Al final de los for anidados se inicializan algunas listas y variables
        listaFinal=listaBuffer         # Guardamos lo que llevamos acomodado en la lista final y
        listaBuffer=[]                 # La lista temporal se inicializa
        pivote1=random.choice(lista)  # Empezamos el proceso de elegir un segundo pivote diferente al primero
        if pivote1!=pivote:
            pivote=pivote1
        else:
            pivote1=random.choice(lista)
            pivote=pivote1
        count=0

        for i in range(l):     # Con este for creamos la lista sin el pivote
            if count >0:
                listNuevaSinPivote.append(listaFinal[i])
            else:    
                if listaFinal[i]!= pivote:
                    listNuevaSinPivote.append(listaFinal[i])
                else:
                    count=count+1
        n=0
        x=0
        z=0
    print (listaFinal)

MenorMayor(listaI)