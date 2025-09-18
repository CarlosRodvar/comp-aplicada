# p025-verificar-suma.py
#Pide dos nnumeros, los suma y verifica si el resultado es igual a un tercer numero
print('-' +60) 
print('Verificar la suma de los dos numeros igual al tercero?\n')
print('-' +60) 

print ('Dame tres numeros enteros:')
n1=int(input('Número 1: '))
n2=int(input('Número 2: '))
n3=int(input('Número 3: '))


suma=n1+n2
if suma==n3:
    print(f'\n¡Correcto! {n1} + {n2} es igual a {n3}')
else:
    print(f'\nNo coincide.  {n1} + {n2}, no es igual {n3}')

print('-' +60)
print('Fin del programa')