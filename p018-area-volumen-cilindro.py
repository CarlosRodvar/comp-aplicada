# p018-area-volumen-cilindro
# Calcular el area y el volumen de un cilindro
import math

print('Calcular el area y volumen de un cilindro\n')
radio= float(input('Dame el valor del radio:'))
altura= float(input('Dame el valor de la altura:'))
area=math.pi*radio*(radio+altura)
volumen=math.pi*(radio*radio)*altura

print('El resultado del area es: {:.2f}' .format(area))
print('El resultado del volumen es: {:.2f}' .format(volumen))


