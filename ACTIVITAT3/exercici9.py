# Lista de asignaturas
asignaturas = ["Matemáticas", "Lengua", "Historia", "Ciencias", "Inglés", "Educación Física"]

notas = []

for asignatura in asignaturas:
    while True:
        try:
            nota = float(input(f"Introduce la nota para {asignatura}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Por favor, introduce una nota válida entre 0 y 10.")
        except ValueError:
            print("Por favor, introduce un número válido.")

for i in range(len(asignaturas)):
    print(f"A {asignaturas[i]} ha sacado {notas[i]:.2f}.")



# Diccionario para almacenar las asignaturas y sus notas
notas_asignaturas = {}

asignaturas = ["Matemáticas", "Lengua", "Historia", "Ciencias", "Inglés", "Educación Física"]

for asignatura in asignaturas:
    while True:
        try:
            nota = float(input(f"Introduce la nota para {asignatura}: "))
            if 0 <= nota <= 10:
                notas_asignaturas[asignatura] = nota
                break
            else:
                print("Por favor, introduce una nota válida entre 0 y 10.")
        except ValueError:
            print("Por favor, introduce un número válido.")

for asignatura, nota in notas_asignaturas.items():
    print(f"A {asignatura} ha sacado {nota:.2f}.")
