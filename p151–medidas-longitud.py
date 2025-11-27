# p151–medidas-longitud.py

def pulgadas_a_centimetros(pulgadas):
    return pulgadas * 2.54


def metros_a_pies(metros):
    return metros * 3.281

while True:
    print("*** Conversor de Unidades ***")
    print("1. Pulgadas a Centímetros")
    print("2. Metros a Pies")
    print("3. Salir")

    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        pulgadas = float(input("Introduce la cantidad en pulgadas: "))
        cm = pulgadas_a_centimetros(pulgadas)
        print(f"{pulgadas} pulgadas equivalen a {cm} centímetros.\n")

    elif opcion == 2:
        metros = float(input("Introduce la cantidad en metros: "))
        pies = metros_a_pies(metros)
        print(f"{metros} metros equivalen a {pies} pies.\n")

    elif opcion == 3:
        print("Saliendo del programa...")
        break

    else:
        print("Opción no válida. Intenta de nuevo.\n")
