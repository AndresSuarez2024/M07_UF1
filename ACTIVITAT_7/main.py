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
        
        if choice == "1":
            name = input("Introduzca el nombre del producto: ")
            description = input("Introduzca la descripción del producto: ")
            price = float(input("Introduzca el precio del producto: "))
            quantity = int(input("Introduzca la cantidad del producto: "))
            create_product(name, description, price, quantity)
        
        elif choice == "2":
            read_products()
        
        elif choice == "3":
            id = int(input("Introduzca el ID del producto para actualizar: "))
            name = input("Introduzca el nuevo nombre: ")
            description = input("Introduzca una nueva descripción: ")
            price = input("Introduzca el nuevo precio: ")
            quantity = input("Introduzca nueva cantidad: ")
            update_product(id, name or None, description or None, float(price) if price else None, int(quantity) if quantity else None)
        
        elif choice == "4":
            id = int(input("Introduzca el ID del producto para eliminarlo: "))
            delete_product(id)
        
        elif choice == "5":
            print("Saliendo...")
            break
        
        else:
            print("Opción no válida, inténtalo de nuevo.")

if __name__ == "__main__":
    menu()
