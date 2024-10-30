"""
Hacer un programa que invierta una palabra
"""
palabra = [str(a) for a in input().lower()]

"""
capicua = ""
j = 0
for i in palabra:
    capicua = capicua + palabra[-1 - j]
    j = j + 1

print(capicua)
"""

def foo(palabra):
    capicua = ""
    j = 0
    for i in palabra:
        capicua = capicua + palabra [-1 -j]
        j = j + 1
    return capicua

print(foo(palabra))

