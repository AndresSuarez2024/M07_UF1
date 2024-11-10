# Se importan las funciones
from create import create_product
from read import read_products
from update import update_product
from delete import delete_product

def menu():
    while True:
        print("\nCRUD Menu:")
        print("1. Create Producto")
        print("2. Read Producto")
        print("3. Update Producto")
        print("4. Delete Producto")
        print("5. Salir")
        
        choice = input("Elige una opción: ")
        
        # Si el usuario elige la opción 1 (Crear producto) ejecuta el bloque correspondiente.
        if choice == "1":
            name = input("Introduzca el nombre del producto: ")
            description = input("Introduzca la descripción del producto: ")
            price = float(input("Introduzca el precio del producto: "))
            quantity = int(input("Introduzca la cantidad del producto: "))
            create_product(name, description, price, quantity)
        
        # Si el usuario elige la opción 2 (Leer producto), ejecuta el bloque correspondiente.
        elif choice == "2":
            read_products()
        
        # permite al usuario actualizar un producto existente en la base de datos. Primero, se pide al usuario el ID del producto y 
        # luego se le solicita que ingrese los nuevos valores para los campos que quiere actualizar
        elif choice == "3":
            id = int(input("Introduzca el ID del producto para actualizar: "))
            name = input("Introduzca el nuevo nombre: ")
            description = input("Introduzca una nueva descripción: ")
            price = input("Introduzca el nuevo precio: ")
            quantity = input("Introduzca nueva cantidad: ")
            # Llama a la función 'update_product' con los nuevos datos. 
            update_product(id, name or None, description or None, float(price) if price else None, int(quantity) if quantity else None)
        
        # Si el usuario elige la opción 4 pide el ID del producto que se desea eliminar.
        elif choice == "4":
            id = int(input("Introduzca el ID del producto para eliminarlo: "))
            delete_product(id)
        
        # Si el usuario elige la opción 5 (Salir), se sale del bucle y termina el programa.
        elif choice == "5":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida, inténtalo de nuevo.")

# Asegura que el menú solo se ejecutará si este archivo se ejecuta directamente
if __name__ == "__main__":
    menu()
