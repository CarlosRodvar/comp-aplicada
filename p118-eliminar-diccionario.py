# p118-eliminar-diccionario.py
# eliminar diccionario

print ()

municipios = {
    'Apozol': 1863,
    'Calera': 1868,
    'Fresnillo': 1554,
    'Guadalupe': 1821,
    'Jalpa': 1824,
    'Jerez': 1824,
    'Loreto': 1931,
    'Mazapil': 1824,
    'Momax': 1857
}

print("Diccionario inicial:")
print(municipios)

del municipios['Apozol']
print("\nDespués de 'del Apozol':")
print(municipios)
municipios.pop('Fresnillo')
print("\nDespués de 'pop(Fresnillo)':")
print(municipios)
municipios.popitem()
print("\nDespués de 'popitem()' (eliminando Momax):")
print(municipios)
municipios.clear()
print("\nDespues de 'clear()':")
print(municipios)
