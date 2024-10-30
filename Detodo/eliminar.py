#Imprimir una lista de numeros a partir de una lista de entrada el cual no debe contener ninguna ocurrencia con el 
# número del segundo input.

inp = input("Escribe una cadena de numeros: ")
inp2 = input(" Escribe un numero el cual va a borrar las coincidencias de la cadena de numeros previa: ")
#inpS = inp.split(" ")
final = []

for i in inp:
    if i != inp2:
        final.append(i)
        
print(final)
