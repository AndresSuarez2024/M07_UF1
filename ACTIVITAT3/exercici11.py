divisas = {
    "Euro": "€",
    "Dólar": "$",
    "Yen": "¥",
    "Libra Esterlina": "£",
    "Franco Suizo": "CHF",
    "Coroa Sueca": "kr"
}

divisa_input = input("Introduce el nombre de una divisa: ")

simbolo = divisas.get(divisa_input)

if simbolo:
    print(f"El símbolo de {divisa_input} es: {simbolo}")
else:
    print("La divisa introducida no está en el diccionario.")
