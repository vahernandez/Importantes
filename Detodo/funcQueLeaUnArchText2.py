"""
Función que lea un archivo de texto
"""

def leer(x):
    with open (x, "r") as cache1:
        cache2 = cache1.readlines()
    for i in cache2:
        i = i.replace("\n", "")
        print(i)
leer("C:\inputs\leer2.txt")