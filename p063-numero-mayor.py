# p063-numero-mayor.py
# Leer una serie de números hasta que el usuario ingrese un 0. Al terminar, 
# el programa deberá mostrar cuál fue el número más grande de todos los introducidos.

print('\033[H\033[J')
while True:
    numero = int(input("\nIngrese un número (0 para terminar): "))

    if numero == 0:
        print("No se ingresaron números.")
    else:
        mayor = numero
        while numero != 0:
            numero = int(input("Ingrese otro número (0 para terminar): "))
            if numero > mayor:
                mayor = numero

        print(f"\nEl número más grande ingresado es: {mayor}")

    if input('\n\nDeseas Continuar (S/N)? ').upper()=='N': break