# p016-tercer-angulo.py
# Calcular el valor de angulo faltante, pidiendo dos valores de angulos.

angulo1=float(input('Dame el valor del primer angulo: '))
angulo2=float(input('Dame el valor del segundo angulo: '))

angulo3= 180- (angulo1+angulo2)

print('El valor del angulo faltante es: {:.2f} grados' .format(angulo3))

