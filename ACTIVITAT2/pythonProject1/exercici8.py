entrada = input("Introduzca entre 1 y 3 palabras: ")

palabras = entrada.split()

if 1 <= len(palabras) <= 3:
    for palabra in palabras:
        longitud = len(palabra)
        primer_caracter = palabra[0]
        ultimo_caracter = palabra[-1]

        print("Palabra: '" + palabra + "'")
        print("Número de caracteres: " + str(longitud))
        print("Primer carácter: '" + primer_caracter + "'")
        print("Último carácter: '" + ultimo_caracter + "'")
        print()
