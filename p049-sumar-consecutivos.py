# p049-sumar-consecutivos.py
# Suma números hasta que el total sea >= 100.
c = 0
suma = 0
print(" Rifa entre amigos para recaudar 100, cuantos boletoss necesito...")

while c < 200:
    c += 1
    suma += c
    print(f" ({c})", end="")

    if suma >= 100:
        print("\n\n ¡Meta alcanzada!")
        print(f'Boletos: {c}')

        break


print(f"Proceso terminado  "+ str(suma))