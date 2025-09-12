# p009-promedio-de-calificaciones.py
#Calcular el promedio de tres calificaciones ingresadas por el usuario

print('Calculando el promedio de tres calificaciones: \n')
#solicitar 3 calificaciones separados por espacio 
cal1, cal2, cal3 = input().split()
print (type(cal1), type(cal2), type(cal3))

cal1, cal2,cal3 =int(cal1), int (cal2), int(cal3) #Convertir cada variable de cadena entero
print (type(cal1), type(cal2), type(cal3))

#calcilar promedio
suma= (cal1+cal2+cal3)
promedio= suma/3
#mostrar el resultafo incluyendo las clasificaciones
print(f'Las calificaciones son {cal1},{cal2},{cal3}')
print (f'La suma : {suma}')
print(f'El promedio de las calificaciones es: {promedio}')



