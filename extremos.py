def extremos (a, b):
    final = []
    cuenta = 0
    while a <= b:
        dicc = {a:a-1}
        final.append(dicc)
        a = a + 1
    return final
print (extremos(2, 6))