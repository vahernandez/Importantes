"""
Hacer un programa que invierta una palabra
"""

def foo (palabra):
    capicua = ''
    j = -1
    for i in palabra:
        capicua = capicua + palabra[j]
        j += -1
    return capicua
print("El capicua es: \n ", foo([str(a) for a in input("Escribe una palabra: \n").lower()]))