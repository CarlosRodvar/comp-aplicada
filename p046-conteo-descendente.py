# p046-conteo-descendente.py
# imprime los numeros del 100 al 1, usando el ciclo while

print('\033[2J\033[H')
print('Iniciando cuenta regresiva')

c=100
while c>=1:
    print(f'{c}', end='')
    c-=1   

print('\nProceso terminado.')