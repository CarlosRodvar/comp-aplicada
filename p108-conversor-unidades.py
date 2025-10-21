# p108-conversor-unidades.py
# Conversor de unidades de longitud a metros usando diccionarios
print('\033[H\033[J')
print('Conversor de unidades de longitud usando diccionarios\n')
conversiones = {
'km': 1000,
'm': 1,
'cm': 0.01,
'mm': 0.001
}
while True: 
    try:
        longitud = int(input("Dame la longitud ?"))
        break
    except ValueError:
        continue
while True: 
            unidad = input("Unidad (km, m, cm ,mm) ? ")
            if unidad in conversiones: break
            else: continue
resultado = longitud / conversiones[unidad]
print(f"{longitud:,.2f} {unidad} son {resultado:,.2f} metros")