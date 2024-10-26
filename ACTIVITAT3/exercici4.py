numeros = input("Introduce 10 números separados por un espacio: ")

numeros_lista = list(map(int, numeros.split()))

if len(numeros_lista) == 10:
    numeros_ordenados = tuple(sorted(numeros_lista))
    print("La tupla ordenada es:", numeros_ordenados)
else:
    print("Debes introducir 10 números.")
