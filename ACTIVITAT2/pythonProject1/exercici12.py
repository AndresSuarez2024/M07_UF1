numero = int(input("Introduce un número: "))

suma = 0

for i in range(1, numero + 1):
    suma += i

print("La suma de todos los números desde el 1 hasta el", numero, "es:", suma)
