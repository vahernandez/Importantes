# Leer dos arreglos, imprimir todas las posiciones donde dos datos en ambos arreglos son iguales ejemp
# [1 5 3 8]
# [4 5 2 8]
# respuesta: [1 3]

primer = input("Escribir una cadena de numeros separadas por un espacio: \n")
primerS = primer.split(" ")
segundo = input("Escribir una cadena de numeros separados por un espacion: \n")
segundoS = segundo.split(" ")
respuesta = []
i = 0   # Este es el indice de ambas lista
for vP in primerS:
    for vS in segundoS:
        print(primerS[i])
        print(segundoS[i])
        if primerS[i] == segundoS[i] :    # Comparamos el valor de ambas lista en la misma posición
            respuesta.append(vP)  # si ambos valores en la misma posicón son iguales entonces append y salimos del for
            break    
        else:
            pass
    i += 1      # Cuando se acaba el segundo for o el for anidado el numero de indice aumenta en uno
print(respuesta)  
    