"""
Hacer un programa que invierta una palabra
"""



palabra = [str(a) for a in input().lower()]
def foo (palabra):
    inv = ""
    j = 0
    for i in palabra:
        inv = inv + (palabra[-1 - j])  # primer iteración = -1, segunda iteración -2 (osea -1 -1), tercera iteración -3 y asi cuantas lentras tenga la palabra del input
        j += 1
    return inv

print(foo(palabra))

    