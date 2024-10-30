
def contar (filee):
    with open(filee, "r") as cache1:
        cache2 = cache1.readlines()
    total = 0
    for i in cache2:
        cuenta = 0
        words = i.split()
        for j in words:
            cuenta = cuenta + 1
        total = total + cuenta
    return total
filee= "C:\inputs\palabras.txt"
print(contar(filee))    