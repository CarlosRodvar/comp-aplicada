# p100-listas-multiplica.py
# Leer dos listas con 5 elementos numéricos y multiplicarlas
print('\033[H\033[J')

listaA = []
listaB = []
listaC = []

print("Introduce 5 números para la Lista A:")
i = 0
while i < 5:
    num = float(input("A[" + str(i+1) + "]: "))
    listaA.append(num)
    i += 1

print("\nIntroduce 5 números para la Lista B:")
i = 0
while i < 5:
    num = float(input("B[" + str(i+1) + "]: "))
    listaB.append(num)
    i += 1

for i in range(5):
    listaC.append(listaA[i] * listaB[i])


print("\n--- Resultados ---")
print("Lista A:", listaA)
print("Lista B:", listaB)
print("Lista C (A * B):", listaC)
