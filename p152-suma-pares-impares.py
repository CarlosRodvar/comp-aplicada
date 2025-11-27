# p152-suma-pares-impares.py

def suma_en_rango(inicio, fin, tipo):
    """
    Suma números pares o impares en el rango [inicio, fin].
    tipo = 'P' para pares, 'I' para impares.
    """
    suma = 0
    tipo = tipo.upper() 

    for n in range(inicio, fin + 1):
        if tipo == 'P' and n % 2 == 0:
            suma += n
        elif tipo == 'I' and n % 2 != 0:
            suma += n

    return suma



print("*** Suma en Rango ***")

inicio = int(input("Introduce el número inicial: "))
fin = int(input("Introduce el número final: "))
opcion = input("¿Qué deseas sumar? (P)ares o (I)mpares: ").upper()

if opcion not in ['P', 'I']:
    print("Error: Debes elegir 'P' para pares o 'I' para impares.")
else:
    resultado = suma_en_rango(inicio, fin, opcion)

    if opcion == 'P':
        print(f"La suma de los números pares entre {inicio} y {fin} es: {resultado}")
    else:
        print(f"La suma de los números impares entre {inicio} y {fin} es: {resultado}")

