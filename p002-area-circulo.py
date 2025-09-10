# p002-area-circulo
# Calcula el area de un circulo area = (Pi * r * r)

import math # importamos el modulo math para constantes y funciones matematicas
print ("calculando el area de un circulo: \n")

#entrada 
print ("Dame el radio: ")
radio = float ( input ())

#proceso 
area = math.pi * math.pow(radio, 2)

# salida
print(f"El circulo de radio {radio: .2f} tiene un area de {area:.2f}")
