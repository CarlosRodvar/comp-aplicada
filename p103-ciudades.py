# p103-ciudades.py
# Programa para leer nombres de ciudades hasta que se ingrese "$"
print('\033[H\033[J')
ciudades = []

while True:
    ciudad = input("Introduzca nombre de ciudad ($ para detener): ")

    if ciudad == "$":
        break

    if ciudad != "":
        ciudades.append(ciudad)
if len(ciudades) == 0:
    print("No se introdujeron ciudades.")
else:
    ordenadas = ciudades[:] 
    n = len(ordenadas)


    for i in range(n - 1):
        for j in range(i + 1, n):
            if ordenadas[i] < ordenadas[j]:
                aux = ordenadas[i]
                ordenadas[i] = ordenadas[j]
                ordenadas[j] = aux


    consonantes = []
    for c in ciudades:
        inicial = c[0].upper()
        if inicial != "A" and inicial != "E" and inicial != "I" and inicial != "O" and inicial != "U":
            consonantes.append(c)

    print("\n--- Resultados ---")
    print("Total de ciudades introducidas:", len(ciudades))
    print("Lista original:", ciudades)
    print("\nLista ordenada descendente:", ordenadas)
    print("\nCiudades que inician con consonante:", len(consonantes))
    print("Lista de ciudades con consonante inicial:", consonantes)
