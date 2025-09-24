# p034-tipo-angulo.py
# Mostrar el tipo de ángulo según su medida en grados.
# <90 agudo, =90 Recto, <180 obtuso, =180 llano, <360 concavo, =360 completo

print ('\033[2J\033[H')
print('--- Clasificador de Ángulos de acuerdo a su magnitud')

angulo = int(input('Dame un ángulo en grados: '))
if angulo < 0 or angulo >= 360:
    print(f'Tu angulo de {angulo} grados, no esta en el rango 0 a 360, por lo tanto es Invalido')
else:
    if angulo<90:
        print(' El ángulo está fuera del rango de 0 a 360 grados.')
    elif angulo < 90:
        print(f' El ángulo de {angulo} grados es un ángulo AGUDO.')
    elif angulo == 90:
        print(f' El ángulo de {angulo} grados es un ángulo RECTO.')
    elif angulo < 180:
        print(f' El ángulo de {angulo} grados es un ángulo OBTUSO.')
    elif angulo == 180:
        print(f' El ángulo de {angulo} grados es un ángulo LLANO.')
    elif angulo < 360:
        print(f' El ángulo de {angulo} grados es un ángulo CÓNCAVO.')
    else:
        print(f' El ángulo de {angulo} grados es un ángulo COMPLETO.')

print('\nProceso terminado.')