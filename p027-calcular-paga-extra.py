#  p027-calcular-paga-extra.py
# Calcula la paga de un trabajador considerando horas extra.


print("\033[2J\033[H", end="")
print('Calculando la paga de un trabajador ')

# Entrada
print("Introduce los datos del trabajador: \n")
nombre = input('Nombre: ')
horas = int(input('Horas trabajadas: '))
paga_hora = float(input('Paga por hora: '))


# proceos
horas_normales = 40
paga_normal = 0
paga_extra = 0
total=0

if horas <= horas_normales:
    paga_normal = horas * paga_hora
    total=paga_normal
else:
    paga_normal = horas_normales * paga_hora
    horas_extra = horas - horas_normales
    paga_extra = horas_extra * (paga_hora * 2)
    total = paga_normal + paga_extra

print("\n Cálculo completo.")
print(f'\n {nombre} trabajo {horas_normales} horas, a una paga de {paga_normal} por hora, horas extra  {horas_extra}.')
print(f'Paga normal = ${paga_normal:13,.2f}')
print(f'Paga extra = ${paga_extra:13,.2f}')
print(f'El pago total = ${total:13,.2f}')

print('\n* ¡Programa finalizado! *')