palabra1 = input("Introduzca la primera palabra: ")
palabra2 = input("Introduzca la segunda palabra: ")

if len(palabra1) >= 2 and len(palabra2) >= 2:
    nueva_palabra1 = palabra2[:2] + palabra1[2:]
    nueva_palabra2 = palabra1[:2] + palabra2[2:]

    print("Resultado:")
    print("Primera palabra intercambiada:", nueva_palabra1)
    print("Segunda palabra intercambiada:", nueva_palabra2)