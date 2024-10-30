

listas = [input() for _ in range(5)] # capturamos los 5 renglones

dicc = {}

for i in range(5):  # en este for creamos 5 listas, le asignamos un renglon a cada lista y convertimos
    dicc[f'lista{i + 1}'] = [int(a) for a in listas[i].split()] # los caracteres de cada renglon a enteros
# estas dos datos osea el numero de una lista y el contenido de esa lista multiplicada por 5
# lo acomodamos en un diccionario


offset = [2, 1, 0, 1, 2]

cont = 0
ext = 0

for i in dicc:
    if 1 in dicc[i]: # 1 en el CONTENIDO del VALOR de cada elemento del diccionario, NO el INDICE
        for j in dicc[i]:
            if 1 == j:
                print(offset[ext] + abs(2-cont))
                cont += 1
    ext += 1  # se pone en este nivel porque es el nivel de if que pregunta si un elemento del diccionario
    # tiene o no un numero 1, independientemente de que si tiene o no tiene este incremento debe darse.


    