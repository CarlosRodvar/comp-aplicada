# p079-factorial-numeros.py
# Calcula el factorial de n números
# Imprime el factorial de los números desde 1 hasta n
print('\033[H\033[J')
print("--- Cálculo Sucesivo de Factoriales ---\n")


print("Calcular el factorial de 1 a n ")
n=8
for i in range(1, n + 1):
    factorial = 1 

    for j in range(1, i + 1):
        factorial *= j

    print(f"El factorial de {i}! es = {factorial}")

print("Error: Por favor, introduce un número entero válido.")