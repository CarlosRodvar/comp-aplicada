# p065-sistema-papeleria.py
# Una papelería necesita un programa para gestionar eficientemente el control de sus ventas de fotocopias.
# Desarrollador: Carlos Abraham Rodriguez Vargas

print('\033[H\033[J')
print('--------------------------------------')
print ("\nSistema de Gestión de Ventas de Fotocopias\n")
print('--------------------------------------')

# Entrada
precio_carta=3
precio_oficio=5
precio_dobleoficio=6
precio_plano=12

copias_carta=0
copias_oficio=0
copias_dobleoficio=0
copias_plano=0
ventas=0

total_carta=0
total_oficio=0
total_dobleoficio=0
total_plano=0
total_ventas=0
 #-----Proceso----- 
while True:
    
    print(f'\nVenta {ventas}')
    print('\nTipo de copia: ')
    print('1. Carta ($3 por copia)')
    print('2. Oficio ($5 por copia)')
    print('3. Doble Oficio ($6 por copia)')
    print('4. Plano ($12 por copia)')
    print('5. Salir y mostrar resumen de ventas')

    opcion=int(input('\nSeleccione el tipo de copia (1-5):  '))
    if opcion == 5:
        break
    cantidad = int(input('\nIngrese la cantidad de copias: '))
    ventas +=1
    # Aplicación de descuento por compra mayor a 50 copias
    descuento=0
    if cantidad>50:
        descuento=0.10
        print('--------------------------------------')
        print('\nSe aplicará un descuento del 10% por comprar más de 50 copias.')
        print('--------------------------------------')
    # Procedimiento de la venta
    if opcion == 1:
        subtotal = cantidad * precio_carta
        subtotal_con_desc = subtotal - (subtotal * descuento)
        total_carta += subtotal_con_desc
        copias_carta += cantidad
        print('--------------------------------------')
        print(f"Subtotal (sin descuento): ${subtotal:.2f}  ->  Con descuento: ${subtotal_con_desc:.2f}")
        print('--------------------------------------')
    elif opcion == 2:
        subtotal = cantidad * precio_oficio
        subtotal_con_desc = subtotal - (subtotal * descuento)
        total_oficio += subtotal_con_desc
        copias_oficio += cantidad
        print('--------------------------------------')
        print(f"Subtotal (sin descuento): ${subtotal:.2f}  ->  Con descuento: ${subtotal_con_desc:.2f}")
        print('--------------------------------------')
    elif opcion == 3:
        subtotal = cantidad * precio_dobleoficio
        subtotal_con_desc = subtotal - (subtotal * descuento)
        total_dobleoficio += subtotal_con_desc
        copias_dobleoficio += cantidad
        print('--------------------------------------')
        print(f"Subtotal (sin descuento): ${subtotal:.2f}  ->  Con descuento: ${subtotal_con_desc:.2f}")
        print('--------------------------------------')
    elif opcion == 4:
        subtotal = cantidad * precio_plano
        subtotal_con_desc = subtotal - (subtotal * descuento)
        total_plano += subtotal_con_desc
        copias_plano += cantidad
        print('--------------------------------------')
        print(f"Subtotal (sin descuento): ${subtotal:.2f}  ->  Con descuento: ${subtotal_con_desc:.2f}")
        print('--------------------------------------')
    else:
        print("Opción no válida, inténtalo de nuevo.")
   
# Cálculo del total de ventas
    total_ventas = total_carta + total_oficio + total_dobleoficio + total_plano
    print(f'Total acumulado de ventas: ${total_ventas:.2f}')
    # -----Salidas-----
print('--------------------------------------')
print('\nResumen de Ventas:')
print('--------------------------------------')
print(f'Ventas realizadas: {ventas}')
print(f'Total por {copias_carta} copias de Carta: ${total_carta:.2f}')
print(f'Total por {copias_oficio} copias de Oficio: ${total_oficio:.2f}')
print(f'Total por {copias_dobleoficio} copias de Doble Oficio: ${total_dobleoficio:.2f}')
print(f'Total por {copias_plano} copias de Plano: ${total_plano:.2f}')
print('--------------------------------------')
print(f'Total general de ventas: ${total_ventas:.2f}')


#Clasificación de desempeño
if total_ventas<50:
    print('\nClasificación: Venta Moderada \n')
elif total_ventas<=150:
    print('\nClasificación: Venta Frecuente\n')
else:
    print('\nClasificación: Venta Superada\n')
print("\nProceso terminado")


