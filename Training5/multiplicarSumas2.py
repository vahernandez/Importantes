"""
Realizar un programa que multiplique dos numeros sin usar el operador de multiplicación
"""

def foo (a, b):
    final = 0
    for i in range(b):
        final = a + final
    return final

print(foo(2, 3))