# p060-promedio-suma.py
# Leer números introducidos por el usuario hasta que ingrese un 0. Al finalizar, 
# mostrar el conteo total de números, la suma y el promedio de la serie.}

print('\033[H\033[J')
while True:
    numero = int(input("\nIngrese un número (0 para terminar): "))

    conteo = 0
    suma = 0

    while numero != 0:
        conteo += 1
        suma += numero
        numero = int(input("Ingrese otro número (0 para terminar): "))

    if conteo > 0:
        promedio = suma / conteo
        print(f"\nConteo total de números: {conteo}")
        print(f"Suma de los números: {suma}")
        print(f"Promedio de la serie: {promedio:.2f}")
    else:
        print("\nNo se ingresaron números.")

    if input('\n\nDeseas Continuar (S/N)? ').upper()=='N': break
print("\nProceso terminado")