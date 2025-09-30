# p059-pares-descendente.py
# imprime los números pares del n al 100 en orden descendente y que sume los pares

print('\033[H\033[J')
while True:
    n = int(input("\nIngrese un número: "))

    i = 100
    suma_pares = 0

    print(f"Números pares entre 100 y {n} :")

    while i >= n:
        if i % 2 == 0:
            print(i, end=" ")
            suma_pares += i
        i -= 1

    print(f"\nLa suma de los números pares es: {suma_pares}")

    if input('\n\nDeseas Continuar (S/N)? ').upper()=='N': break       
print("\nProceso terminado")



