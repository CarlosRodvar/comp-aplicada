# p090-triangulo-invertido-numeros.py
# Imprime triangulo invertido de numeros


print('\033[H\033[J')
n = int(input("Dame un número: "))

print()  # Línea en blanco antes del triángulo

for i in range(n, 0, -1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()