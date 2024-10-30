# Buscar cuantos problemas se pueden resolver en un examen, hay 3 personas, si a simple vista
# dos de estas personas consideran que pueden resolver un problema, entonces se marca como problema
# resuelto, si por el contrario si solo una persona o ninguna considera que puede resolver un problema
# contará como problema no resuelto. 

# Entradas como ejemplo: 
# Primer entrada
# 3 Problemas
# 1 1 0
# 1 1 1
# 1 0 0
#
# Segunda entrada 
# 2 problemas
# 1 0 0
# 0 1 1

# Solución 1, si el input fuera de la siguiente manera:

# Entradas como ejemplo: 
# Primer entrada
# 3 Problemas
# 110
# 111
# 100
# Es decir que los unos y ceros no tengan espacios usariamos la siguiente solución:


n = int(input())

respuesta = 0
for i in range(n):
    linea = input()  # En este caso como no pusimos split y si ponemos de entrada 1 0 1 los espacios los llevara a comparar a los if y hara mala lectura
    cuentaUnos = 0
    print(linea[0])
    print(linea[1])
    print(linea[2])
    if linea[0] == '1':
        cuentaUnos +=1
    if linea[1] == '1':
        cuentaUnos += 1
    if linea[2] == '1':
        cuentaUnos +=1
    if cuentaUnos >= 2:
        respuesta +=1
print(respuesta)

"""

# Solución 2
si las entradas de 1s y 0x si tienen espacios usamos split:

n = int(input())
respuesta = 0
for i in range(n):
    calif = input()
    valor = calif.split(' ')
    contador=0
    if valor[0] == '1':
        contador += 1
    if valor[1] == '1':
        contador += 1
    if valor[2] == '1':
        contador +=1
    if contador >= 2:
        respuesta += 1
print(respuesta)
        
"""