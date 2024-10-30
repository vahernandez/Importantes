# Basic Calc

print("Hola esta es una calculadora basica")
#print(" Teclea una opción que quieras realizar:")

while True:
    opcion = int(input("Teclea una opción que quieras realizar: \n 1 para suma \n 2 para resta \n 3 para multiplicar: \n 4 o cualquier otro número para salir: \n"))
    if opcion == 1:
        n1 = int(input("teclea el primer número: \n"))
        n2 = int(input("teclea el segundo número: \n"))
        print("El resultado de esta suma es: ", n1+n2)
    elif opcion == 2:
        n1 = int(input("teclea el primer número: \n"))
        n2 = int(input("teclea el segundo número: \n"))
        print("El resultado de esta suma es: ", n1-n2)
    elif opcion == 3:
        n1 = int(input("teclea el primer número: \n"))
        n2 = int(input("teclea el segundo número: \n"))
        print("El resultado de esta suma es: ",  "ATENCION EL RESULTADO ES: >>>>  ", n1*n2, "  <<<<<<", "\n")
    else:
        print( "Adios")
        break