# Realiza un programa que sume todos los números enteros pares desde el 0 hasta el 100

lista = []
i=0

while i <= 20:
    lista.append(i)
    i +=2
suma = 0
for j in lista:
    suma=j+suma
print(suma)
    
