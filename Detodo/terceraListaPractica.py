# Dadas dos listas, debes generar una tercera lista con todos los elementos que se repitan en ellas, pero no debe repetirse ningun elemento en la nueva lista.

lista1= ["h", "o", "l", "a", " ", "m", "u", "n", "d", "o"]
lista2= ["h", "o", "l", "a", " ", "l", "u", "n", "a"]

lista3= []

for i in lista1:
    if i not in lista2:
        lista3.append(i)
print(lista3)