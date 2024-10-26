contactos = {}

while True:
    nombre = input("Introduce el nombre del contacto (o escribe 'no' para finalizar): ").strip()

    if nombre.lower() == 'no':
        break

    if nombre in contactos:
        print("Este nombre ya existe en el diccionario. No se añadirá.")
        continue

    try:
        edad = int(input("Introduce la edad de {}: ".format(nombre)))
    except ValueError:
        print("Por favor, introduce un número válido para la edad.")
        continue

    contactos[nombre] = edad
    print("Contacto añadido correctamente.")

print("\nDiccionario de contactos:")
for nombre, edad in contactos.items():
    print(f"{nombre}: {edad}")
