# p010-operaciones-matematicas.py
#Demostrar el uso de los diferentes operadores aritmeticos con numero

print('='*80)
print('Calculadora de operaciones matematicas')
print('='*80)
#entrada
x=float(input('Valor de x?'))
y=float(input('Valor de y ?'))

#salida
print(f'Suma: {x:>15,.2f} +{y:<15,.2f}= {x+y:>15,.2f}')
print(f'Resta: {x:>15,.2f} +{y:<15,.2f}= {x-y:>15,.2f}')
print (f'Multiplicación: {x:>15,.2f} * {y:<15,.2f} ={x-y:>15,.2f}')
print (f'División: {x:>15,.2f} / {y:<15,.2f} ={x-y:>15.2f}')
print (f'Módulo: {x:>15,.2f} % {y:<15,.2f} ={x-y:>15.2f}')
print (f'Exponenciación: {x:>15,.2f} ^ {y:<15,.2f} ={x-y:>15.2f}')
print (f'División entera: {x:>15,.2f} // {y:<15,.2f} ={x-y:>15.2f}')
print('='*80)