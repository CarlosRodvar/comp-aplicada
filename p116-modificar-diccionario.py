# p116-modificar-diccionario.py
# Modificar valores en un diccionario existente

print ('\033[H\033[J')

print ('Modificar Diccionario\n')
paises={
    'Argentina': 100,
    'Brasil': 200,
    'Colombia': 300,
    'Chile': 400,
    'Ecuador': 500,
    'Bolivia': 600,
    'Jamaica': 700
}

print('Diccionario inicial:')
print(paises)

print('\nModificando valores en el diccionario:')
paises['Brasil'] = 250
paises['Chile'] = 450
paises.update({'Bolivia': 650, 'Jamaica': 750})

print('Diccionario modificado:')
print(paises)
