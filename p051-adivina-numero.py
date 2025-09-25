# p051-adivina-numero.py
# Simula un juego de azar donde el usuario adivina un numero entre 1 y 50

import random
print('\033[2J\033[H')
print('Bienvenido al juego de adivina numero')
print('Yo te doy un numero entre el 1 y 50 y tu tratas de adivinarlo')

numero_secreto= random.randint(1,50)
intento= 0
contador_intentos=0

while True:
    intento=int(input('Cual es tu intento?'))
    contador_intentos +=1
    if intento < numero_secreto:
        print('DEmasiado bajo, intenta con un numero mas alto')
    elif intento > numero_secreto:
        print('Demasiado alto, intenta con un numero mas bajo')
    else:
        print(f'\nFelicidades, adivinaste el número secreto, era {numero_secreto}')
        print(f'Lo lograste en {contador_intentos} intentos!')
        break   

print('\nHaya sido como haya sido ya terminamos.')