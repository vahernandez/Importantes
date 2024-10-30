from DeployFunctions import *
# Escribir un prgrama que permita procesar datos de pasajeros de viaje en una lista de tuplas con la siguiente forma: (nombre, dni, destino). ejem:
# [("Manuel Juarez", 19823451, "Liverpool"), ("Silvana Paredes", 22709128, "Buenos Aires"), ("Rosa Ortiz", 15123978, "Glasgow"), ("Luciana Hdz", 38981374), "Lisboa")]
# Además, en otra lista de tuplas se almacenan los datos de cada ciudad y el país al que pertenecen. Ejem:
#
# [("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), ("Lisboa", "Portugal"), ("Liverpool", "Inglaterra"), ("Madrid", "España")]
# Hacer un menú iterativo que permita al usuario realizar las siguientes operaciones:
# * Agregar pasajeros a la lista de viajeros.
# * Agregar ciudades a la lista de ciudades.
# * Dado el DNI de un pasajero, ver a qué ciudad viaja
# * Dada una ciudad, mostrar la cantidad de pasajeros que viajan a esa ciudad.
# * Dado el DNI de un pasajero, ver a que país viaja.
# * Dado el país, mostrar cuántos pasajeros viajan a ese país.
# * Salir del programa
pasajeros = []
ciudades = []

while True:
    print ("1. Agregar pasajeros")
    print ("2. Agregar ciudades")
    print ("3. Buscar ciudad destino mediante el DNI")
    print ("4. Cantidad de pasajeros que viajan a una ciudad")
    print ("5. Buscar país destino mediante DNI")
    print ("6. Cantidad de Pasajeros que viajan a un país")
    print ("7. Salir del programa")
    opcion = int(input("Acción a ejecutar: \n"))


    if opcion == 1:
        print("Agregar pasajeros \n")
        pasajeros = agregarPasajeros(pasajeros)  # pasarle la version nueva de la lista de pasajeros para que reemplace la original
        print(pasajeros)
        
    elif opcion ==2:
        print ( "Agregar Ciudades \n ")
        ciudades = agregarCiudades(ciudades)
        print(ciudades)
    
    elif opcion ==3:
        dni = int(input("\n ***** Cual es el número de DNI? \n"))
        print("\n  ***** El pasajero con dni", dni, "viaja a: ", buscarCiudad(pasajeros, dni), "\n")
    
    elif opcion == 4:
        ciudad = input("Ciudad: ")
        print("Viajan", cantidadPasajerosCiudad(pasajeros, ciudad), "pasajeros")
        
   
    elif opcion == 5:
        dni = int(input("DNI: "))
        print("Viaja a", buscarPaisDestino(pasajeros, ciudades, dni))  
   
    elif opcion == 6:
        pais = input("País: ")
        print("Viajan", cantidadPasajerosPais(pasajeros, ciudades, pais), "pasajeros")
        
    elif opcion == 7:
        break
    
    else:
        print ("Opcion invalida")  
        break

    



   
        
        
