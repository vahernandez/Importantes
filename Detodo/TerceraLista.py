# Dadas dos listas, debes generar una tercera lista con todos los elementos que se repitan en ellas, pero no debe repetirse ningun elemento en la nueva lista.

lista1= ["h", "o", "l", "a", " ", "m", "u", "n", "d", "o"]
lista2= ["h", "o", "l", "a", " ", "l", "u", "n", "a"]

lista3= []
for i in lista1:
    if i in lista2 and i not in lista3:  # el i busca en toda la lista2 y la lista3, eso ayuda en que en un enunciado
        lista3.append(i)                # se haga la operación principal
print(lista3)

