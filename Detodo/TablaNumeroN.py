"""
Imprime la tabla de un numero n
"""

n = int(input("¿De que número quisieras que se creara una tabla de multiplicar? \n"))

for i in range(1,11):
    #print(n, "x", i, "=", (i*n))
    print(f"{n} x {i} = {n*i}")

