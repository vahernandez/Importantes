# Imprime la tabla de multiplicar de un numero N"


N = int(input("Que numero te gustaría realizar la tabla?: \n"))

for i in range(10):
    tabla = N * i 
    print(N, "x", i, " = ", tabla)


