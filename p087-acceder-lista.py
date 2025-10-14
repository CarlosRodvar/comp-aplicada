# p087-acceder-lista.py
# accedere a ñps eñementos de una ñista por su indice

nums=[10,20,30,40,60,70,10,20,99]

print('Acceder a los elementos de una lista')
print ('\nLongitud y contenido')
print(f'Cuantas mediciones son: {len(nums)}')
print(f'Todas las mediciones: {nums}')

print('\nPrimera y ultima medicion, por indice positivo')
print(f'La primera: {nums[0]}')
print(f'La ultima: {nums[len(nums)-1]}')

print('\nPrimera y ultima medicion, por indice negativo')
print(f'La primera: {nums[-len(nums)]}')
print(f'La ultima: {nums[-1]}')

print('\Por rango: ')
print (f'Los primeros 3: {nums[0:3]}')
print (f'Los ultimos 3: {nums[-3:]}')

print (f'Los del medio: {nums[3:6]}')
