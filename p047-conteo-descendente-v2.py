# p047-conteo-descendente-v2.py
# imprime los numeros del 100 al 1, usando el ciclo while

print('\033[2J\033[H')
print('Iniciando cuenta regresiva')
n=int(input('Desde donde  '))
m= int(input('de cuanto en cuanto  '))

c=n
while c>=1:
    print(f' {c} ' , end=' ')
    c-=m   

print('\nProceso terminado.')