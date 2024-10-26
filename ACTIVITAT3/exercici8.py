entrada = input("Introduce 10 números separados por espacios: ")

numeros_lista = list(map(float, entrada.split()))

if len(numeros_lista) != 10:
    print("Debes introducir exactamente 10 números.")
else:
    suma_total = sum(numeros_lista)
    mitjana = suma_total / len(numeros_lista)

    numeros_lista.append(suma_total)
    numeros_lista.append(mitjana)

    print("Números de l’usuari:", numeros_lista[:-2])
    print("Suma total:", suma_total)
    print("Mitjana:", mitjana)
    print("Lista completa (incluyendo suma y media):", numeros_lista)
