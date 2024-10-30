f1 = input()
f2 = input()
f3 = input()
f4 = input()
f5 = input()

lista = []
fS1 = f1.split(" ")
lista.append(fS1)
fS2 = f2.split(" ")
lista.append(fS2)
fS3 = f3.split(" ")
lista.append(fS3)
fS4 = f4.split(" ")
lista.append(fS4)
fS5 = f5.split(" ")
lista.append(fS5)

yy = 0
indX = 2
indY = 2
xx = 0
cont = []
for j in lista:
    print(j)
    for i in lista[yy]:
        if '1' in j and '1' == j[xx]:
            cont.append(int(abs(indX)))
            cont.append(int(abs(indY)))
            break
        else:
            pass
        xx += 1
        indX -= 1
    xx = 0
    indX = 2
    indY -= 1
    yy += 1   
final= 0
for n in cont:
    final = final + n

print(final)
    
    



    