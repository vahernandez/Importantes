# Realizar un cuadrado de 10 x 5 pero con la circunferencia de unos y la parte interna con 0 ceros.

unos = 111111111111111
unosCeros = 100000000000001
cont = 0

for j in range(5):
    if cont == 0 or cont == 4:
        print(unos)
    else:
        print(unosCeros)
    cont +=1

