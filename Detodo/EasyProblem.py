cuantos = int(input())
binario = [int(a) for a in input().split(" ")]
suma = 0
for i in binario:
    suma = i + suma
if suma == 0:
    print('EASY')
else:
    print('HARD')
    