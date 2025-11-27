# p149–numero-menor.py
def menor_de_tres():
    # La función pide los 3 números y devuelve el menor
    n1 = int(input("Introduce el primer número: "))
    n2 = int(input("Introduce el segundo número: "))
    n3 = int(input("Introduce el tercer número: "))

    # Calculamos el menor
    menor = n1  # suponemos que el primero es el menor

    if n2 < menor:
        menor = n2
    if n3 < menor:
        menor = n3

    return menor


# Programa principal
menor = menor_de_tres()
print("El número menor es:", menor)
