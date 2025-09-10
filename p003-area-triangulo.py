# p003-area-triangulo.py
# Calcula el area de un triangulo

print ("Calcula el area de un triangulo \n:")

print("Dame la base y la altura separados por enter")
base, altura= int(input ()), int (input()) #lee dos valores

# proceso
area= (base *altura ) /2

#salida
print ('El triangulo de base :',  base)
print ('El triangulo de altura :',  altura)
print ('Tiene de area ',  area)

print (f'\nEl trinagulo de base {base} y altura {altura} tiene un area de {area:,.2f}')

print ('El trinagulo de base ' + str(base) + ' y altura  ' + str(altura)+ ' tiene un area de  ' +str(area))
