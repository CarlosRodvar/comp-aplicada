# p155-estadisticas-basicas.py

import math

def leer_lista_enteros():
    """
    Lee una línea de números separados por espacio
    y devuelve una lista de enteros.
    """
    entrada = input("Dame números (separados por espacio): ")
    partes = entrada.split()
    numeros = [int(x) for x in partes]
    return numeros


def numero_mayor(lista):
    return max(lista)


def numero_menor(lista):
    return min(lista)


def media(lista):
    return sum(lista) / len(lista)


def varianza_poblacional(lista):
    """
    Varianza poblacional: divide entre N (no entre N-1).
    """
    m = media(lista)
    suma_cuadrados = 0
    for x in lista:
        suma_cuadrados += (x - m) ** 2
    return suma_cuadrados / len(lista)


def desviacion_estandar_poblacional(lista):
    """
    Desviación estándar poblacional: raíz cuadrada de la varianza poblacional.
    """
    return math.sqrt(varianza_poblacional(lista))



numeros = leer_lista_enteros()

print("Lista de números:", numeros)
print("Estadísticas:")

m = media(numeros)
mayor = numero_mayor(numeros)
menor = numero_menor(numeros)
var = varianza_poblacional(numeros)
desv = desviacion_estandar_poblacional(numeros)

print(f"La media: {m:.3f}")
print(f"Mayor de los datos: {mayor}")
print(f"Menor de los datos: {menor}")
print(f"Varianza: {var:.3f}")
print(f"Desviación estándar: {desv:.3f}")
