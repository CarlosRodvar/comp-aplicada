# p014-funciones-trigonometricas.py
# Demostrar el uso de funciones trigonometricas básicas

import math

#definir un angulo en grados y convertirlo a radianes
angulo=45
radianes=math.radians(angulo)
                       
# Calcular funciones trigonométricas básicas
seno=math.sin(radianes)
coseno=math.cos(radianes)
tangente=math.tan(radianes)

#convertr de vuelta a grados para demostración
grados=math.degrees(radianes)

#Formatear la salida con f-strings para mejpr presentaci+on
salida= ('Resumen de funciones\n')
f'El seno es {seno:.4f}\n'
f'El coseno es {coseno:.4f}\n'
f'La tangente es {tangente:.4f}\n'
f'El angulo {angulo} grados, en radianes equivale a {radianes:.4f}\n'
f'Los {radianes:.4f} radianes equivalen a {grados:.4f}\n'

#mostrar salida formateada
print (salida)
