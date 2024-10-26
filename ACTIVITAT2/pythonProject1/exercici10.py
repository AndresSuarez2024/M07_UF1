import random

numero_secreto = random.randint(1, 100)

intentos = 0

print("Intenta adivinar el número que estoy pensando entre 1 y 100.")

intento = int(input("Introduce un número: "))

while intento != numero_secreto:
    intentos += 1

    if intento < numero_secreto:
        print("¡El número es mayor!")
    elif intento > numero_secreto:
        print("¡El número es menor!")

    intento = int(input("Introduce un número: "))

intentos += 1
print("Has acertado el número.")
print("Número de intentos: ", intentos)
