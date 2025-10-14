# p087-plan-ahorro-depistos-mensuales.py
#simulara un plan de ahorro

print('\033[H\033[J')
print("--- Simulador de Plan de Ahorro ---\n")

monto_inicial = float(input("¿Cuál es tu monto inicial?: "))
aporte_mensual = float(input("Ingresa un depósito mensual fijo: "))
tasa_interes = float(input("Ingresa la tasa de interés mensual (en porcentaje): "))
meses = int(input("¿Por cuántos meses planeas ahorrar?: "))

print("\n--- Plan de Ahorro Detallado ---")

monto_ahorrado = monto_inicial

for mes in range(1, meses + 1):
    saldo_inicial = monto_ahorrado
    interes = saldo_inicial * (tasa_interes / 100)
    saldo_final = saldo_inicial + interes + aporte_mensual
    
    print(f"Mes {mes}: Saldo Inicial: ${saldo_inicial:.2f} | Interés: ${interes:.2f} | Saldo Final: ${saldo_final:.2f}")
    
    monto_ahorrado = saldo_final

print("\nSaldo final después de", meses, "meses: $", round(monto_ahorrado, 2))
