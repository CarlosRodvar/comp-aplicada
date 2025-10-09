# p072-suma-pares-impares.py
# Imprimir los números pares y números impares , su suma también en un rango determinado
while(True):
    print('\033[H\033[J')
    print('Imprimir la suma de pares e impares en un rango de 1 a n')
    print('[1] Pares')
    print('[2] Impares')
    op=int(input('Elige? '))

    s=0

    if op==1:
        print('\nImprimiendo numeros pares y su suma')
        n=int(input('\nLimite ? '))
        for i in range(2, n +1, 2):
            print(i, end='')
            s += i
        print('\suma  de pares:'+ str(s))
    elif op==2:
        print(f'\nImprimir numeros impares y su suma')
        n = int(input('Limite? '))
        for i in range(n, +1, 2):
            print(i, end=' ')
            s += i
        print('\suma  de impares:'+ str(s))

    else:
        print('\nOpción No valida')

    if input('\n\nDeseas continuar (S/N) ? ').upper()=='N': break
print('\nHemos llegado al final ....')