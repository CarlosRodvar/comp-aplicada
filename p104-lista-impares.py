#p104-lista-impares.py

print('\033[H\033[J')

n = int(input("Introduzca la cantidad de números impares (n): "))
impares = []
num = 1
contador = 0
while contador < n:
    impares.append(num)
    num += 2
    contador += 1

print("\n--- Generación de Lista ---")
print("Lista de los primeros", n, "números impares:", impares)
suma = 0
for x in impares:
    suma += x

promedio = suma / len(impares)

print("\n--- Cálculos ---")
print("Suma de los números:", suma)
print("Promedio de los números:", promedio)

div3 = []
for x in impares:
    if x % 3 == 0:
        div3.append(x)

suma_div3 = 0
for x in div3:
    suma_div3 += x

print("\n--- Divisibles entre 3 ---")
print("Números divisibles entre 3:", div3)
print("Suma de los números divisibles entre 3:", suma_div3)

buscar = int(input("\n--- Búsqueda ---\nIntroduzca elemento a buscar: "))

encontrado = False
posicion = -1
for i in range(len(impares)):
    if impares[i] == buscar:
        encontrado = True
        posicion = i
        break

if encontrado:
    print("Resultado: El elemento", buscar, "está en la lista en la posición (índice)", posicion, ".")
else:
    print("Resultado: El elemento", buscar, "NO está en la lista.")



