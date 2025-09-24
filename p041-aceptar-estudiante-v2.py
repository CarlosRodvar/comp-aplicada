# p041-aceptar-estudiante-v2
# Programa que solicite nombre, sexo, edad y tres calificaciones a un estudiante.
# Si es mujer, es mayor de 21 de edad y su promedio esta entre 8 -9.5, se le acepta.

print('\033[2J\033[H')
print('Aceptacion Universidad Kitty Kat SA')

nombre = input('Dame tu nombre: ')
sexo = input('Dame tu sexo (H/M): ').upper()  
edad = int(input('Dame tu edad: '))
print('Dame 3 calificaciones (0 a 10):')
c1, c2, c3 = input().split()
c1, c2, c3 = float(c1), float(c2), float(c3)
promedio = (c1 + c2 + c3) / 3
print(f' El promedio es: {promedio:.2f}')
if sexo == 'M' and edad >= 21 and 8 <= promedio <= 9.5:
    print(f' ¡Felicidades, {nombre}! Has sido aceptada en la Universidad Kitty Kat SA. Con un promedio de{promedio:.2f}.')
elif sexo == 'H':
    print(f' Lo sentimos, {nombre}. Solo aceptamos mujeres.')
elif edad < 21:
    print(f' Lo sentimos, {nombre}. Solo aceptamos mayores de 21 años.')   
elif promedio < 8 or promedio > 9.5:
    print(f' Lo sentimos, {nombre}. El promedio debe estar entre 8 y 9.5.')
else:
    print(f' Lo sentimos, {nombre}. No cumples con los requisitos para ser aceptada.')  
print('\nProceso terminado.')
