frase = input("Introduce una frase: ")

frase_sin_espacios = tuple(frase.replace(" ", ""))

print("Contenido de la tupla:", frase_sin_espacios)

frase_sin_repetidos = "".join(dict.fromkeys(frase_sin_espacios))

print("Frase sin caracteres repetidos:", frase_sin_repetidos)
