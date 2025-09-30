# p058-impares-ascendente.py
# imprime los números impares del 1 al n en orden ascendente y que sume los impares
print('\033[H\033[J')
while True:
    n = int(input("\nIngrese un número entero positivo: "))

    i = 1
    suma_impares = 0

    print(f"Números impares entre 1 y {n}:")

    while i <= n:
        if i % 2 != 0:
            print(i, end=" ")
            suma_impares += i
        i += 1

    print(f"\nLa suma de los números impares es: {suma_impares}")

    if input('\n\nDeseas Continuar (S/N)? ').upper()=='N': break       
print("\nProceso terminado")
