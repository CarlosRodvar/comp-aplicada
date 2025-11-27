# p153-suma-digitos.py

def leer_lista_enteros():
    """
    Lee una línea de números separados por espacio
    y devuelve una lista de enteros.
    """
    entrada = input("Dame los números (separados por espacio): ")
    lista = entrada.split()          
    numeros = [int(x) for x in lista]  
    return numeros


def suma_digitos(n):
    """
    Recibe un entero y devuelve la suma de sus dígitos.
    Ejemplo: 1971 -> 1 + 9 + 7 + 1 = 18
    """
    n = abs(n)  # por si hubiera negativos
    suma = 0
    while n > 0:
        suma += n % 10   # último dígito
        n //= 10         # quita el último dígito
    return suma


def lista_sumas_digitos(lista_numeros):
    """
    Recibe una lista de enteros y devuelve una nueva lista
    con la suma de los dígitos de cada número.
    """
    nueva_lista = []
    for num in lista_numeros:
        nueva_lista.append(suma_digitos(num))
    return nueva_lista


# Programa principal
numeros = leer_lista_enteros()
resultado = lista_sumas_digitos(numeros)

print("La lista de números original :", numeros)
print("La lista con las suma de dígitos de los números:", resultado)

