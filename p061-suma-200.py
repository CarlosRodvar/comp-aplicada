# p061-suma-200.py
# Leer números y sumarlos hasta que el total acumulado sea mayor o igual a 200. Al terminar, 
# mostrar cuántos números se introdujeron y la suma final.

print('\033[H\033[J')
while True:
    suma = 0
    conteo = 0

    while suma < 200:
        numero = int(input(f"Suma actual: {suma}. Introduce un número: "))
        suma += numero
        conteo += 1

    print(f"\nSe introdujeron {conteo} números.")
    print(f"La suma final es: {suma}")

    if input('\n\nDeseas Continuar (S/N)? ').upper()=='N': break
print("\nProceso terminado")
