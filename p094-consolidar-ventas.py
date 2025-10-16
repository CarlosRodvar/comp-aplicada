# p094-consolidar-ventas.py
# Consolidar las ventas de dos sucursales, usando listas

print('\033[H\033[J')
print('Consolidar ventas de dos sucursales\n')
elementos=int(input('¿Cuantas ventas diarias se registrara?'))

ventas_suc1=[]
ventas_suc2=[]
ventas_consolidadas=[]

print('\n Registrando ventas de la sucursal 1:')
for i in range (elementos):
    venta= int(input (f'Venta del dia {i+1}:'))
    ventas_suc2.append(venta)

for i in range(elementos):
    suma_dia=ventas_suc1[i]+ ventas_suc2[i]
    ventas_consolidadas.append(suma_dia)

    print('\n---Reporte de ventas ---')
    print(f'Sucursal 1: {ventas_suc1}')
    print(f'Sucursal 2: {ventas_suc2}')
    print(f'Ventas Consolidadas: {ventas_consolidadas}')

