# p064-verificar-palindromo.py
# Solicitar al usuario que ingrese un número entero y determinar si es un palíndromo. 
# Un número es palíndromo si se lee igual de izquierda a derecha que de derecha a izquierda (ej. 121, 3443).

print('\033[H\033[J')
while True:
    numero = input("\nIngrese un número entero: ")

    if numero == numero[::-1]:
        print(f"\nEl número {numero} es un palíndromo.")
    else:
        print(f"\nEl número {numero} no es un palíndromo.")

    if input('\n\nDeseas Continuar (S/N)? ').upper()=='N': break
print("\nProceso terminado")
