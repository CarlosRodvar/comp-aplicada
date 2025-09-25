# p050-conteo-numeros.py
# Permite ingresar n numeros, se detiene al introducir 999 y muestra estadisticas

print('\033[2J\033[H')
print('Estadisticas con numeros que el usuario proporciona')

cuenta=0
suma=0
cp=0

while True:
    num= int(input('Introduce un numero'))
    if num== 999:
        print('Detectando sentinela 999, me voy')
        break
    cuenta+=1
    suma +=num
    if num>0:
            cp+=1
    elif num<0:
            cn+=1
    else:
            cz+=1


print('\n RESUMEN FINAL')
print(f'Numeros introducidos {cuenta} ')
print(f'La suma es: {suma}')
print(f'Positivos: {cp}')
print(f'Negativos: {cn}')
print(f'Ceros: {cz}')
