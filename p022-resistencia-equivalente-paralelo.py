# p022-resistencia-equivalente-paralelo.py
# Calcular la resistencia equivalente en un circuito paralelo, pidiendo los valores de las resistencias.

print('Calcular la resistencia equivalente en un circuito paralelo\n')


R1 = float(input('Dame el valor de la resistencia R1 (en ohmios): '))
R2 = float(input('Dame el valor de la resistencia R2 (en ohmios): '))
R3 = float(input('Dame el valor de la resistencia R3 (en ohmios): '))
R4 = float(input('Dame el valor de la resistencia R4 (en ohmios): '))


Requivalente = 1 / (1/R1 + 1/R2 + 1/R3+ 1/R4) 


#salida
print('El valor de la resistencia equivalente es: {:.2f} ohmios' .format(Requivalente))


