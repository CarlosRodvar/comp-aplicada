#p015-hipotenusa-triangulo.py
#Calcular a hipotenusa de um triangulo , dando los valores de dos catetos.
import math

cateto1 = float(input("Digite el valor de primer cateto: "))
cateto2 = float(input("Digite el valor de segundo cateto: "))        

hipotenusa = math.sqrt(cateto1**2 + cateto2**2) 

print('Valor de la hipotenusa es: {:.2f}'.format(hipotenusa))