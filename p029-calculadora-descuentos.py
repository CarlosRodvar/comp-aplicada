# p029-calculadora-descuentos.py
# Simula una calculadora de descuentos basada en el monto de la compra

print("Calculadora de Descuentos \n")
compra = float(input("Ingresa el total de tu compra: $"))


descuento = 0
porcentaje = 0

if compra > 2000:
    porcentaje = 0.20
else:
    if compra > 1000:
        porcentaje = 0.10 
    else:
        if compra > 500:
            porcentaje = 0.05 
        else:
            descuento = 0

descuento=compra*porcentaje
total = compra - descuento
print('Resumen Final')
print(f'Total de la compra.  :{compra}')
print(f'Porcentaje de descuento  :{porcentaje*100}%')
print(f'Descuento.  :{descuento}')
print(f'Total a pagar.  :{total}')

print('\nProceso terminado')