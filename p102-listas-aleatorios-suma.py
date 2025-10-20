# p102-listas-aleatorios-suma.py
# Generar listas A y B con 10 números aleatorios cada una
print('\033[H\033[J')

import random
listaA = []
listaB = []
listaC = []


for i in range(10):
    listaA.append(random.randint(1, 100))
    listaB.append(random.randint(1, 100))

# Crear lista C con la suma solo si ambos son impares
for i in range(10):
    a = listaA[i]
    b = listaB[i]
    if a % 2 != 0 and b % 2 != 0:
        listaC.append(a + b)
    else:
        listaC.append(0)

# Mostrar resultados
print("--- Listas Generadas ---")
print("Lista A:", listaA)
print("Lista B:", listaB)
print("\n--- Resultados (Suma solo si A[i] y B[i] son ambos impares) ---")
print("Lista C:", listaC)
