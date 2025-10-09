# p077-triangulo-caracter.py
# Imprime un triángulo rectángulo de caracter deseado

print('\033[H\033[J')
print('Imprime un triángulo rectángulo de caracter deseado')

n = int(input("¿Cuántos renglones? "))
c = input("¿Qué carácter quieres? ")



# Bucle exterior se
for i in range(1, n + 1):
# Bucle interior: controla las columnas (o caracteres por fila)
# El rango llega hasta 'i' para que cada fila tenga 'i' caracteres
    for j in range(1, i):
# 'aqui se ejecutan las acciones anidadas
        print(f'{c}', end="")
# 'print()' genera el siguiente nivel
print()