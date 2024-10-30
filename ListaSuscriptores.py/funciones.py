def creaSuscriptores(suscriptores):
    # Esta función creará una lista de suscptores.
    nombre = input("Teclea un nombre de un subscritor nuevo, si quieres salir teclea la letra x: \n")
    while nombre != "x":
        id = input("Teclea su Id: \n")
        plan = input("Teclea su nivel de subscripción: \n")
        suscriptores.append((nombre, id, plan))
        nombre = input("Teclea otro nombre si quieres seguir agregando o teclea x si quieres salir: \n")
    return suscriptores    
    
def creaPlanes(planes):
    # Esta función creará una lista de planes de subscripción
    plan = input("")