#p099-procesar-notas.py
# Procesar notas de estudiantes en una lista
print('\033[H\033[J')
print('Procesador de notas de estudiantes\n')
notas = []  # lista para guardar las notas

while True:
    nota = float(input("Introduce una nota (0 para terminar): "))

    # validar rango
    if nota < 0 or nota > 100:
        print("❌ Error: la nota debe estar entre 0 y 100.")
        continue  # volver a pedir la nota

    # condición de parada
    if nota == 0:
        break

    notas.append(nota)

# verificar si hay notas ingresadas
if len(notas) == 0:
    print("No se introdujeron notas.")
else:
    # cálculos
    suma = 0
    for n in notas:
        suma += n

    promedio = suma / len(notas)

    maximo = notas[0]
    minimo = notas[0]
    for n in notas:
        if n > maximo:
            maximo = n
        elif n < minimo:
            minimo = n

    menores_promedio = []
    for n in notas:
        if n < promedio:
            menores_promedio.append(n)

    # resultados
    print("\n--- Resultados ---")
    print("Total de notas introducidas:", len(notas))
    print("Lista de notas:", notas)
    print("Suma de notas:", suma)
    print("Promedio de notas:", promedio)
    print("Nota máxima:", maximo)
    print("Nota mínima:", minimo)
    print("Cantidad de notas menores al promedio:", len(menores_promedio))
    print("Lista de notas menores al promedio:", menores_promedio)

