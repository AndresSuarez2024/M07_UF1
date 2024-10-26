num = int(input("Introduce un número entre 10 y 100: "))

if 10 <= num <= 100:
    numeros = tuple(range(1, num + 1))
    print("La tupla creada és:", numeros)
else:
    print("El número introducido no está dentro del rango permitido.")
