# p031-2da-ley-de-newton.py
# Calcular la segunda ley de newton
# fuerza=masa* aceleracion, masa=fuerza / aceleracion, aceleracion=fuerza /masa


print('--- Calculadora de la 2da Ley de Newton ---')
print('[F] Calcular la Fuerza (fuerza = masa * aceleración)')
print('[M] Calcular la Masa (masa = fuerza / aceleración)')
print('[A] Calcular la Aceleración (aceleración = fuerza / masa)')
opcion = input('Elige una opción (F, M o A): ').upper()
                   
# La estructura if/elif/else ejecuta el cálculo correcto
if opcion == 'F':
    print('\n Calculando la Fuerza...')
    masa = float(input('Dame la masa: '))
    aceleracion = float(input('Dame la aceleración: '))
    fuerza = masa * aceleracion
    print(f' La fuerza es: {fuerza} ')
elif opcion == 'M':
    print('\n Calculando la Masa...')
    fuerza = float(input('Dame la fuerza: '))
    aceleracion = float(input('Dame la aceleración: '))
    masa = fuerza / aceleracion
    print(f' La masa es: {masa} ')
elif opcion == 'A':
    print('\n Calculando la Aceleración...')
    fuerza = float(input('Dame la fuerza: '))
    masa = float(input('Dame la masa: '))
    aceleracion = fuerza / masa
    print(f' La aceleración es: {aceleracion} ')
else:
    print('\n Opción inválida.  elige F, M o A.')

print('\nProceso terminado.')