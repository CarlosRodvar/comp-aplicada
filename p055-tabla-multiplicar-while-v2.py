# p055-tabla-multiplicar-while-v2.py
# Imprime todas las tablas de multiplicar desde la 1 hasta la n, desde el 1 hasta el m
while(True):
    print('\033[H\033[J')
    print('Tablas de Multiplicar')
    while True:
        n = int(input('Hasta que tabla quieres ? '))
        m = int(input('Hasta donde la quieres ? '))
        if n>0 and m>0: break

        print('Error, vslores incorrectos')
    t = 1
    while t <= n:
        print(f'\nTabla del {t} \n')
        c=1
        while( c <= m ):
            print(f'{t} x {c} = {t*c}')
            c+=1
        t+=1
    if input('\n\nDeseas Continuar (S/N)? ').upper()=='N': break

print("\nProceso terminado.")