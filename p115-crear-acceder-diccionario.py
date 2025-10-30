# p115-crear-acceder-diccionario.py
# crear un diccionario de dias de la semana

print ('\033[H\033[J')
print ('Diccionario de Días de la Semana\n')

dias_semana = {
    1: 'Lunes',
    2: 'Martes',
    3: 'Miércoles',
    4: 'Jueves',
    5: 'Viernes',
    6: 'Sábado',
    7: 'Domingo'
}

print('Diccionario inicial:')
print(dias_semana)

print('\nAccediendo a los elementos:')

print(f"Llave 1 : {dias_semana[1]}")
print(f"Llave 7 : {dias_semana[7]}")
print(f"Llave 5 : {dias_semana.get(5)}")
print(f"Llave 7 : {dias_semana.get(7)}")


print('Diccionario final:')
print(dias_semana)