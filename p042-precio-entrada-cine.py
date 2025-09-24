# p042-precio-entrada-cine.py
# Calcular el precio de la entrada al cine según la edad.
# Menores de 5 años gratis, de 5 a 12 años 5 pesos, de 13 a 64 años 10 pesos, mayores de 65 años 7 pesos

print('\033[2J\033[H')
print('--- Precio de la entrada al cine ---')
edad = int(input('Dame tu edad: '))
if edad < 5:
    precio = 0  
elif 5 <= edad <= 12:
    precio = 5
    print(f' El precio de la entrada es: {precio} pesos.')
elif 13 <= edad <= 64:
    precio = 10
    print(f' El precio de la entrada es: {precio} pesos.')
else:
    precio = 7
print(f' El precio de la entrada es: {precio} pesos.')
print('\nProceso terminado.')