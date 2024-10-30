# Realiza un program que lea un numero impar por teclado. Si el usuario no introduce un número impar, debe repetirse el proceso hast que lo intruduzca correctamente.


impar = float(input("Introduce un numero impar: "))

mod = impar % 2
n = 0

while n == 0:   
    if mod != 0:
        print ("El número que tecleaste es impar!")
        n = n + 1
    else:
        print ("El número que tecleaste es par!")
        impar = float(input ("Introduce otro número: "))
        mod = impar % 2
        n = 0
     