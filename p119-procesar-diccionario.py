# p119-procesar-diccionario.py

nombres = ['Juan', 'Pedro', 'Manuel', 'Elias', 'Maria', 'Felipe', 'Julia', 'Roberto']
sueldos = [4550.22, 8456.88, 1235.12, 9998.00, 12345.50, 29456.55, 12234.00, 2000.00]


nomina = dict(zip(nombres, sueldos))


print("Diccionario nómina:")
print(nomina)

print("\n—-- Iterando Llaves (keys) ----")
for k in nomina.keys():
    print(k)

print("\n—--- Iterando Valores (values)----")
for v in nomina.values():
    print(f"{v:.2f}")

print("\n—---- Iterando Llave y Valor (accediendo por llave)----")
for k in nomina:
    print(f"{k}: {nomina[k]:.2f}")

print("\n—---- Iterando Llave y Valor (items)----")
for k, v in nomina.items():
    print(f"{k}: {v:.2f}")
total = sum(nomina.values())
promedio = total / len(nomina)

print('\n --- Cálculos ---')
print(f"\nSuma total de sueldos: {total:.2f}")
print(f"Promedio de sueldos: {promedio:.2f}")
