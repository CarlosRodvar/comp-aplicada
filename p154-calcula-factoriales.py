# p154-calcula-factoriales.py

def leer_lista_enteros():
    """
    Lee una línea de números separados por espacio
    y devuelve una lista de enteros.
    """
    entrada = input("Dame los números (separados por espacio): ")
    partes = entrada.split()
    numeros = [int(x) for x in partes]
    return numeros


def factorial(n):
    """
    Recibe un entero n y devuelve su factorial.
    Ejemplo: 5 -> 120
    """
    if n < 0:
        raise ValueError("El factorial no está definido para negativos.")
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado


def lista_factoriales(lista_numeros):
    """
    Recibe una lista de enteros y devuelve una nueva lista
    con el factorial de cada número.
    """
    nueva_lista = []
    for num in lista_numeros:
        nueva_lista.append(factorial(num))
    return nueva_lista


numeros = leer_lista_enteros()
factoriales = lista_factoriales(numeros)

print("La lista de números originales:", numeros)
print("La lista con los factoriales:", factoriales)
