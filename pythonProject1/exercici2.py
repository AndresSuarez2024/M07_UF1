valor = float(input("Introduce un valor en €: "))

iva = 0
while iva not in [4, 10, 21]:
    iva = int(input("Introduce el IVA a aplicar: "))
    if iva not in [4, 10, 21]:
        print("Porcentaje de IVA no válido. ")

valor_final = valor + (valor * iva / 100)

print("Valor inicial: " + str(valor) + " €")
print("% de IVA: " + str(iva) + "%")
print("Valor final con IVA: " + str(valor_final) + " €")

