# Realiza un programa que pida al usuario cuantos números quiere introducir, luego lee todos los números y reaiiza una media aritmética


cuantos = int(input("Cuantos números quieres promediar? \n"))
i=0
array = []
while i <= (cuantos-1):
    num = int(input("Introduce el numero: "))
    array.append(num)
    i = i +1
total = 0   
for j in array:
    total = j + total
print (total/cuantos)
    