"""
Escribir un programa que te convierta el texto que lee en ese mismo texto sin vocales
"""
with open('C:\\inputs\\textoVocales.txt', 'r') as cache1:
    cache2 = cache1.readlines()
    
vocales= ["a", "e", "i", "o", "u"]

with open('C:\\inputs\\textSinVocales.txt', 'w') as cache3:
    for i in cache2:
        linea= [str(a) for a in i.lower()]
        sinVoc =""
        for j in linea:
            if j not in vocales:
                sinVoc = sinVoc + j
        if sinVoc:              # Solo escribir la linea si no esta vacía
            cache3.write(sinVoc + '\n')


