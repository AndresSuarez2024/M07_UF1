abecedario = [chr(i) for i in range(97, 123)]  # Letras de la 'a' a la 'z'

posiciones_a_eliminar = [i for i in range(len(abecedario)) if (i + 1) % 3 == 0]

lista_resultante = [letra for i, letra in enumerate(abecedario) if i not in posiciones_a_eliminar]

tupla_resultante = tuple(lista_resultante)

print("Lista resultante:", lista_resultante)
print("Tupla resultante:", tupla_resultante)
