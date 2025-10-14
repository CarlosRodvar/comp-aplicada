# p090-eliminar-lista.py
# Eliminar elementos de una lista

print('\033[H\033[J')
print('Eliminar elementos de una lista:\n')
nums = [1, 3, 5, 7, 9, 11, 99, 15, 88, 19, 100]
print(f'Datos originales con anomalías: {nums}- {len [nums]}\n')
print(f'Eliminar el valor 99:')
nums.remove(99)
print(f'Resultado : {nums}- {len [nums]}\n')
print(f'Eliminar el elemento en la posición 8')
num_removido = nums.pop(8)
print(f'Resultado : {nums}- {len [nums]}- Se removio ({num_removido}),\n')
print(f'Eliminar el último elemento:')
ultimo_num = nums.pop()
print(f'Resultado : {nums}- {len [nums]}- Se removio ({ultimo_num}),\n')

print(f'Eliminar todos las mediciones')
nums.clear()
print(f'Resultado: {nums}- {len [nums]}\n')
