# menu.py

# Importar las funciones de los otros archivos
from opcion1 import opcion1_func
from opcion2 import opcion2_func

# Definir la función principal del menú
def main_menu():
    print("Menú:")
    print("1. Opción 1")
    print("2. Opción 2")
    print("3. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == '1':
        opcion1_func()
    elif opcion == '2':
        opcion2_func()
    elif opcion == '3':
        print("Saliendo del programa...")
    else:
        print("Opción inválida. Inténtelo de nuevo.")

if __name__ == "__main__":
    main_menu()
