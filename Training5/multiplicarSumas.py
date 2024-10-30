"""
Realizar un programa que multiplique dos numeros sin usar el operador de multiplicación
"""


def foo (a, b):
    tot = 0
    for i in range(b):
        tot = tot + a
    return tot
    
print(foo(5, 7))