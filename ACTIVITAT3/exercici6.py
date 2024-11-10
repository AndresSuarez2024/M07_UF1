areas_piso = ["Salón", 10.15, "Recibidor", 9.56, "Habitación1", 12.34,
              "Terraza", 15.55, "Baño", 7.98, "Cocina", 12, "Habitación2", 12.23]

print("El segundo elemento es:", areas_piso[1])

print("El último elemento es:", areas_piso[-1])

indice_terraza = areas_piso.index("Terraza") + 1
print("El área de la terraza es:", areas_piso[indice_terraza])

print("Del primer al tercer elemento:", areas_piso[:3])

print("Del tercer al último elemento:", areas_piso[2:])

indice_hab1 = areas_piso.index("Habitación1") + 1
indice_hab2 = areas_piso.index("Habitación2") + 1
total_habitaciones = areas_piso[indice_hab1] + areas_piso[indice_hab2]
print("El total del área de las dos habitaciones es:", total_habitaciones)

indice_baño = areas_piso.index("Baño") + 1
areas_piso[indice_baño] = 8.50  # Nuevo valor del área del baño
print("Lista actualizada con el área modificada del baño:", areas_piso)

areas_piso.extend(["Patio interior", 2.78])
print("Lista actualizada con el área del 'patio interior':", areas_piso)

total_area = sum(areas_piso[i] for i in range(1, len(areas_piso), 2))
print("El total del área del piso es:", total_area)
