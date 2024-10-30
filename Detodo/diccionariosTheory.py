# Los diccionarios son una estructura de datos que almacena datos asociados a un indice, la difererencia con las listas es que el indice se puede
# crear y asignarle el valor que queramos ejemplo:
# {'Andre':10} indice : valor 

# puedes crear la posición que quieras: ejemplo puedes crear el indice 10 con valor de 25:

dicc = {}
dicc[10]= 25

print(dicc)

# Un arreglo solo puede tener posiciones numericas enteras, pero el diccionario si puede tener posiciones valores fraccionales y palabras:

dicc = {10:25, 'Andre': 70, 2.99:'Flotante'}

# Imprimir solo los indices(esta es una diferencia con respecto a las listas ya que cuando iteras por una lista el resultado son los valres
# pero en un diccionario cuando iteras el resultado son los indices):
for indices in dicc:
    print(indices)

# Imprimir los valores
for indices in dicc:
    print(dicc[indices])

# Uno de los casos de uso mas comunes de un diccionario es el de registrar cuentas de una situación ejemplo:

dicc = {}

#Registra nombres y edades

dicc['Andre'] = 50
dicc['Valentin'] = 30
dicc['Sebastian'] = 25
dicc['Karen'] = 29

print(dicc['Andre'])   # Si quiero saber el valor de la posición Andre

# Quiero sumarle uno a una persona.
if 'Andre' in dicc:
    dicc['Andre'] += 1
else:
    dicc['Andre'] = 1   # en caso de que Andre no existiese en el diccionario lo crea con valor de uno.

print(dicc['Andre'])






