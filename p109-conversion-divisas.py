# p109-conversion-divisas.py
# Conversor de divisas a pesos mexicanos usando diccionarios

print('\033[H\033[J')
print("Conversor de monedas a pesos mexicanos (MXN)")
conversiones = {
'USD': 20.50,
'EUR': 22.30,
'GBP': 25.80,
'JPY': 0.19,
'CAD': 16.20
}
print("\nOpciones de monedas a pesos mexicanos (MXN): ")
for moneda in conversiones:
    print(f"- {moneda} ")
while True:
    moneda = input("\nIngrese la moneda a convertir: ").upper()
    if moneda in conversiones: break
    continue

while True: 
    try:
        cantidad = float(input(f"Ingrese la cantidad en {moneda}: "))
        if cantidad > 0: break
        continue
    except ValueError:
            print("Entrada no válida.")

resultado = cantidad * conversiones[moneda]
print(f"{cantidad:,.2f} {moneda} son {resultado:,.2f} MXN")