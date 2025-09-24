# p039-numeros-romanos.py
# Convertir un número entero a número romano.
# 4 IV 11 Error

print('\033[2J\033[H')
print('--- Convertir un número entero a número romano ')
print('Dame un número entero entre 1 y 10:')
n = int(input())
if n == 1:
    romano = 'I'   
elif n == 2:
    romano = 'II'
elif n == 3:
    romano = 'III'
elif n == 4:
    romano = 'IV'
elif n == 5:

    romano = 'V'
elif n == 6:
    romano = 'VI' 
elif n == 7:
    romano = 'VII'
elif n == 8:
    romano = 'VIII'
elif n == 9:
    romano = 'IX'
elif n == 10:
    romano = 'X'
else:
    romano = 'Error, el número debe estar entre 1 y 10'
print(f' El número romano es: {romano}.')
print('\nProceso terminado.')
