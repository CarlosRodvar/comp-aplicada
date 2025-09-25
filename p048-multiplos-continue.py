# p048-multiplos-continue.py
# Imprime solo los múltiplos de 10 hasta 200.

print('\033[2J\033[H')
print(" Buscando múltiplos de 10 entre 1 y 200...")

c = 0
while c < 200:
    c += 1
    if c % 10 != 0:

        continue #ignota todo lo que sigue y salta la siguiente iteracion
    #solo se ejecuta el multiplo de 10

    print(f" {c}", end=" ")

print("\n Búsqueda finalizada.")