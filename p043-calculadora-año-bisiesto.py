# p043-calculadora-anio-bisiesto.py 
# Determinar si un año es bisiesto o no, con condiciones es divisible wentr 4 pero no por 100 y otra divisible por 400

print('\033[2J\033[H')
print('--- Determinar si un año es bisiesto o no ')
print('Dame un año (entero):')
anio = int(input())
if (anio % 4 == 0 and anio % 100 != 0):
    print(f' El año {anio} es bisiesto ! (Por que es divisible entre 4 pero no entre 100)')
elif (anio % 400 == 0):
    print(f' El año {anio} es bisiesto ! (Por que es divisible entre 400)')
elif (anio % 100 == 0):
    print(f' El año {anio} no es bisiesto ! (Por que es divisible entre 100 pero no entre 400)')
else:
    print(f' El año {anio} no es bisiesto ! (Por que no es divisible entre 4)')
print('\nProceso terminado.')

