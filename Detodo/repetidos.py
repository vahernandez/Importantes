# dada la lista con la palabra coco, generar otra lista sin los caracteres repetidos.

lista1 = ["c", "o", "c", "o"]
lista2 = []

for i in lista1:
    if i not in lista2:
        lista2.append(i)

print(lista2)       