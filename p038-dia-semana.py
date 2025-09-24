# p038-dia-semana.py
# Escribe un programa que pida un número del 1 al 7 y muestre el día de la semana correspondiente.
# 2 lunes, 8 Error,

print('\033[2J\033[H')
print('--- Día de la semana ')  

print('Dame un número del 1 al 7:')
n = int(input())    

if n == 1:
    dia = 'Lunes'
elif n == 2:
    dia = 'Martes'
elif n == 3:
    dia = 'Miércoles'   
elif n == 4:
    dia = 'Jueves'
elif n == 5:
    dia = 'Viernes'
elif n == 6:
    dia = 'Sábado'
elif n == 7:
    dia = 'Domingo'
else:
    dia = 'Error, el número debe estar entre 1 y 7'
print(f' El día es: {dia}.')
print('\nProceso terminado.')    
