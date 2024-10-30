"""
Crear una función que indique que letras no son vocales en una palabra
"""

with open ("C:\\inputs\\palabras.txt", "r") as cache1:
    cache2 = cache1.readlines()
    
voc = ["a", "e", "i", "o", "u"]
sinVoc = ""
for i in cache2:
    iter = [str(a) for a in i.lower()]
    for j in iter:
        if j not in voc:
             sinVoc = sinVoc + j
print(sinVoc)

        
    
    