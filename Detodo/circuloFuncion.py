import math

def circulo (radio):
    area = math.pi * (radio * radio)
    per = math.pi * 2 * radio
    return area, per

radio = int(input("Teclea el radio: \n"))

a,p = circulo(radio)
print (f"Area: {a}")
print(f"Perimetro: {p}")
