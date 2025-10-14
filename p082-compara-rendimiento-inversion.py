# p082-compara-rendimiento-inversion.py
# Desarrolla un programa que compare el crecimiento de dos fondos de inversión a lo largo de varios años.

print("\033[H\033[J")
print('----Comparacion del crecimiento de dos fondos---')
monto_inicial1=float(input('Ingrese el monto inicial del fondo 1: '))
tasa_interes1=float(input('Ingrese la tasa de interes anual del fondo 1(en porcentaje): '))

monto_inicial2=float(input('Ingrese el monto inicial del fondo 2: '))
tasa_interes2=float(input('Ingrese la tase de interes anual del fondo 2(en porcentaje): '))

años_proy=int(input('Ingrese los años a proyectar: '))

print('\nComparación de fondos de inversión')
print("------------------------------------")

fondo1=monto_inicial1
fondo2=monto_inicial2
año=1

while año<=años_proy:
    fondo1=fondo1+(fondo1 *tasa_interes1/100)
    fondo2=fondo2+(fondo2 *tasa_interes2/100)
    if año==1:
        print('Año\t|Fondo 1\t|Fondo 2')
        print('------------------------------------')
    print(año, '\t|$', round (fondo1, 2), '\t|$', round (fondo2, 2))

    año= año+1

print('\nResultado final: ')
if fondo1>fondo2:
    print('El fondo 1 generó un mayor rendimiento.')
elif fondo2>fondo1:
    print('El fondo 2 generó un mayor rendimiento. ')
else:
    print('Ambos fondos generaron el mismo rendimiento.')
print(f'Fondo 1: {round(fondo1,2)}')
print(f'Fondo 2: {round(fondo2,2)}')
