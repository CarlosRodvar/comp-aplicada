# p040-calculo-notas.py
# calculo de promedio de 5 calificaciones y su respectiva condicion

print('\033[2J\033[H')
print('--- Cálculo de promedio de 5 calificaciones ')

print ('Dame 5 calificaciones (0 a 10):')
c1, c2, c3, c4, c5 = input().split()
c1, c2, c3, c4, c5 = float(c1), float(c2), float(c3), float(c4), float(c5)
promedio = (c1 + c2 + c3 + c4 + c5) / 5
print(f' El promedio es: {promedio:.2f}')
if promedio >= 9:
    print(' ¡Perfecto, tu esfuerzo valio la pena!')
elif promedio >= 8:
    print(' Excelente, sigue asi!')
elif promedio >= 7:
    print(' Muy bien, pero puedes mejorar!')
else:
    print(' Reprobado, necesita tomar el curso nuevamente.')

print('\nProceso terminado.')
