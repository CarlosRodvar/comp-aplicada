# p021-distnacia-entre-puntos.py
#Calcula la distancia entre dos puntos en un plano carte siano

import math
{print('Calcular la distancia entre dos puntos en un plano cartesiano\n')}


xa = float(input('Dame el valor de x del punto A: '))
ya = float(input('Dame el valor de y del punto A: '))
xb = float(input('Dame el valor de x del punto B: '))
yb = float(input('Dame el valor de y del punto B: '))  

distancia = math.sqrt((xa - xb)**2 + (ya - yb)**2)

print('La distancia entre los dos puntos es: {:.2f}' .format(distancia))
