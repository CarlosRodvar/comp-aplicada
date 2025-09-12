# p012-funcion-matematicas-ecuacion.py
#Evaluar la función f(x,y) =3x2 + √(x2 + y2) + e^(ln(x))
# Usando operador de exponenciacion (**) y funcion pow () de math

import math as mt #Importar la biblioteca math para funciones matematicas con un alias 

# Definir los valores de x, y para la evaluación
x=2
y=2

#Evaluar la función usando el operador de exponenciación  (**)
fx_y_star =3*x**2+mt.sqrt(x**2+y**2)+mt.exp(mt.log(x))

fx_y_pow=3*mt.pow(x,2) +mt.sqrt(mt.pow(x,2)+ mt.pow(y,2))+mt.exp(mt.log(x))
print(f'El resultado es : {fx_y_star:.4f}')
print(f'El resultado es : {fx_y_pow:.4f}')
