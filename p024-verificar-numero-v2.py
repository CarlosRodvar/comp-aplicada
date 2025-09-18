# p024-verificar-numero-v2.py4
# Verificar si un número es positivo, negativo o cero(version if else)

print('Verificar si un número es positivo, negativo o cero\n')

#entrada
print('Dame un numero entero:')
numero=int(input())

if numero>0:
    print('El numero es POSITIVO')
else:
    if numero<0:
        print('El numero es NEGATIVO')
    else:
        print('El numero es CERO')

print('\nAqui terminamos de tomar decisiones')
