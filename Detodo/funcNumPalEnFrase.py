"""
Haz una función que pida una frase y devuelva el numero de palabras que tiene
"""

def numero(palabra):
    x = palabra.split()
    #cuenta = 0
    #for i in x:
        #cuenta = cuenta + 1
    return len(x)
print(numero("hola mundo"))

"""

palabra = ("hola mundo")
print (type(palabra))
print(palabra)
x = palabra.split()
print(x)
cuenta = 0
for i in x:
    print (i)
    cuenta = cuenta + 1
print (cuenta)

"""