# vp073-suma-promedio-numeros.py
# Suma de n numeros introducidos por el usuario usando ciclo for

while(True):
    print('\033[H\033[J')
    print('Sumando y promediando numeros')

    
    n = int(input('Cuantos calificaciones ? '))
    suma = 0
    
    for i in range(1, n+1):
        cal = int(input(f'Número[{i}] = '))
        suma += cal
        numeros += str(cal) +''
    print(f'Los numeros que introdujiste fueron: {numeros}')
    print(f'La suma es {suma}, el promedio es {suma / cal}')
    if input('\n\nDeseas continuar (S/N) ? ').upper()=='N': break
print('\nHemos llegado al final ....')