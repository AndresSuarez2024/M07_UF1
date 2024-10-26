num = int(input("Introduce un número entre 1 y 10: "))

if 1 <= num <= 10:
    tabla_multiplicar = [num * i for i in range(1, 11)]
    print("La tabla de multiplicar es:", ', '.join(map(str, tabla_multiplicar)))
else:
    print("El número introducido no está dentro del rango permitido.")
