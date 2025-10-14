# p092-lista-de-gastos.py
# Permite llevar el control de una lista de gasto

print()

gastos=[450.50,120.00,85.90,230.00,55.75]
limite_gasto=100.00

while True:
    print('\n----Menú de Gestión de Gastos---')
    print('1. Ver todos los gastos')
    print('2. Agregar un gasto')
    print('3. Modificarr un gasto existente')
    print('4. Eliminar un gasto')
    print('5. Ver resumen y total de gastos')
    print('6.Salir')
    opcion= int(input('Elige una opcion (1-6): '))

    if opcion==1:
        print('\nLista de gastos:')
        print(gastos)
    elif opcion==2:
        try:
            nuevo_gasto=float(input('Ingresa el monto del nuevo gasto: '))
            gastos.append(nuevo_gasto)
            print(f'Gasto de ${nuevo_gasto} agregado correctamente.')
        except ValueError:
            print('Entrada inválida. Por favor ingresa un número.')
    elif opcion==3:
        try:
            pos=int(input('Ingresa el índice del gasto a modificar (0 a {}): '.format(len(gastos)-1)))
            valor_anterior=gastos[pos]
            print(f'Gasto a modificar gastos[{pos}] ${valor_anterior:.2f}  ')
            nuevo_valor=float(input('Ingresa el nuevo monto del gasto: '))
            gastos[pos]=nuevo_valor     
            print(f'Gasto modificado de {valor_anterior:.2f} a ${nuevo_valor}.')
        except (IndexError):
            print('Error: La posicion esoecificada no se necuentra en la lista')
        except ValueError:
            print('Entrada inválida. Por favor ingresa números válidos.')
    elif opcion==4:
        try:    
            gasto_a_eliminar=float(input('Ingresa el monto del gasto a eliminar: '))
            if gasto_a_eliminar in gastos:
                gastos.remove(gasto_a_eliminar)
                print(f'Gasto de ${gasto_a_eliminar} eliminado correctamente.')
            else:
                print(f'Gasto de ${gasto_a_eliminar} no encontrado en la lista.')
        except ValueError:
            print('Entrada inválida. Por favor ingresa un número válido.')
    elif opcion==5:
            if not gastos:
                print('No hay gastos para mostrar')
            else:
                total_gastado=0
                print('n-- Resumen del mes---')
                for gasto in gastos:
                    total_gastado+=gasto
                    estado='Dentro del limite'
                    if gasto>limite_gasto:
                        estado='Excede el limite'
                    print(f'Gasto: ${gasto:.2f} - {estado}')
                print(f'\nTotal gastado en el mes: ${total_gastado:.2f}')
    elif opcion==6: 
        print('Gracias por usar el gestor de gastos. ¡Hasta luego!')
        break
    else:
        print('Opción inválida. Por favor elige una opción del 1 al 6.')
    input('\nPresiona Enter para continuar...')
    print('\033[H\033[J')
print('Fin del programa')

            
