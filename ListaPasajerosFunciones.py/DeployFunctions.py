
def agregarPasajeros(pasajeros):
    #Agrega pasajeros a la lista y la retorna
    nombre=input(" Teclea nuevo pasajero, si quieres cortar usa la letra x \n")
    while nombre != "x":
        dni = int(input("Agrega su dni: \n"))
        destino = input( "Agrega destino: \n")
        pasajeros.append((nombre, dni, destino))
        print(pasajeros)
        nombre = input("Si quieres seguir agregando pasajeros teclea su nombre y si quieres terminar teclea x \n")
    return pasajeros

def agregarCiudades(ciudades):
    #Agrega ciudades a la lista y la retorna
    capital = input("Teclea el nombre de una ciudad , si quieres terminar usa la letra x \n")
    while capital != "x":
        pais = input("Teclea el país de la ciudad \n")
        ciudades.append((capital, pais))
        print(ciudades)
        capital = input("Si quieres seguir agregando ciudades teclea el nombre de una ciudad y si quieres terminar teclea la letra x \n")
    return ciudades    

def buscarCiudad(pasajeros, dni):   # necesito pasar pasajeros y dni por que los ocupo en la funcion, a pasajeros lo uso para ser la lista iterable y el dni es el dato
    #Dado el DNI de un pasajero, lo busca en la lista y retorna la ciudad a la que viaja
    for i in pasajeros:
        #print(i)
        #print(i[1] )
        if i[1] == dni:
            return i[2]  
    return ""

def cantidadPasajerosCiudad(pasajeros, ciudad):
    #Dada una lista de pasajeros y una ciudad, retorna la cantidad de pasajeros que viajan a esa ciudad.
    cuenta = 0
    for i in pasajeros:
        if i[2] == ciudad:
            cuenta += 1
    return cuenta 
    
def buscarPaisDestino(pasajeros, ciudades, dni):
    # Dada una lista de pasajeros, una de ciudades y un DNI, retorna el país al que viaja el pasajero con ese DNI
    
    for i in pasajeros:
        for j in ciudades:
            if dni==i[1] and i[2] == j[0]:
                return j[1]
                break

def cantidadPasajerosPais(pasajeros, ciudades, pais):
    #Dada una lista de pasajeros, una de ciudades y un país, retorna la cantidad de pasajeros que viajan a ese país
    cuenta = 0
    for i in pasajeros:
        for j in ciudades:
            if pais==j[1] and i[2] == j[0]:
                cuenta = cuenta + 1
    return cuenta
