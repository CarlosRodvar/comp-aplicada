# - p093-procesar-calificaciones.py
# procesa calificaciones en una lista

print('\033[H\033[J')

print('Procesador de calificaciones de un curso\n')
print('Introduce calificaciones entre 0 y 10 (usa para terminar: \n)')

calificaciones = []
suma=0.0
while True:
    try:
        cal=float(input('Calificacion >'))
        if cal ==99: break
        if 0<= cal <=10:
            calificaciones.append(cal)
            suma+= cal
        else:
            print('Error: la calificacion debe estar entre 0 y 10')

    except ValueError:
        print('Entrada no valida. Por favor, introduce un numero')
    if not calificaciones:
        print('No se capturaron calificaciones.')
    else:
        promedio = suma/ len(calificaciones)
        mayores_promedio= []
        for cal in calificaciones:
            if cal > promedio: mayores_promedio.append(cal)
            

        print (f'\n Se capturaron {len (calificaciones)} calificaciones')
        print(f'Las calificaciones son: {calificaciones}')
        print('\n-- Estadisticas del curso ---')
        print (f'Promedio  : {promedio}')
        print(f'Suma totalc: {sum(calificaciones)}')
        print(f'Calificaciones mayores al promedio: {len(mayores_promedio)}->{mayores_promedio}')
        print(f'Calificacion mas alta: {max(calificaciones)}')
        print(f'Calificacion mas baja: {min(calificaciones)}')
