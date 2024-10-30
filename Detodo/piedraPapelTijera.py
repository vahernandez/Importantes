import random

user = input("elije piedra, papel o tijera: ")

maquina = random.choice(["piedra", "papel", "tijera"])
x= "si"
print(maquina)
while x == "si":
    if user == maquina:
        print("empate")
    elif user == "piedra" and maquina == "tijera":
        print("Tu ganas")
    elif user == "tijera" and maquina == "piedra":
        print("Tu pierdes")
    elif user == "papel" and maquina == "piedra":
        print("Tu ganas")
    elif user == "piedra" and maquina == "papel":
        print("Tu pierdes")
    elif user == "tijera" and maquina == "papel":
        print("Tu ganas")
    else:
        print("Tu pierdes")
    x = input("Quieres seguir jugando? \n")
    if x == "si":   
        user = input("elije piedra, papel o tijera: ")
        maquina = random.choice(["piedra", "papel", "tijera"])
        print(maquina)
    else:
        print("hasta luego")
        break
