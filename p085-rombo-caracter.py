# p089-rombo-caracter.py
#Imprime rombo de caracter

print('\033[H\033[J')
n = int(input("Dame un número impar para la altura: "))

# Validar que sea impar
while n % 2 == 0:
    print("El número debe ser impar.")
    n = int(input("Dame un número impar para la altura: "))

caracter = input("¿Qué carácter quieres usar? ")

print()  # Línea en blanco antes del dibujo

# Parte superior del rombo
for i in range(1, n + 1, 2):
    espacios = (n - i) // 2
    print(" " * espacios + caracter * i)

# Parte inferior del rombo
for i in range(n - 2, 0, -2):
    espacios = (n - i) // 2
    print(" " * espacios + caracter * i)
    