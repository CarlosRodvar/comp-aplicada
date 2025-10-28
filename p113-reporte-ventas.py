# p113-reporte-ventas.py
# Crear una lista de diccionarios para representar un reporte de ventas

print('\033[H\033[J')
print('Reporte de Ventas por cliente \n')

print('-'*60)
print("\n--- Registro de Transacciones ---")
n = int(input("Número de compras a registrar: "))
compras = []
for i in range(1,n+1):
    print(f'\n------ Compra {i+1} ------')
    compra = {
        "cliente" : input("Nombre Cliente : "),
        "producto": input("Nombre Producto : "),
        "cantidad": float( input("Cantidad : ")),
        "precio" : float(input("Precio : "))
    }
compras.append(compra)
print('\n--- Lista de Compras Registradas ---\n',compras)
clientes = {} 
for compra in compras:
    cliente = compra["cliente"]
if cliente not in clientes:
    clientes[cliente] = {"cantidad": 0, "subtotal": 0}
    clientes[cliente]["cantidad"] += compra["cantidad"]
    clientes[cliente]["subtotal"] += compra["cantidad"] * compra["precio"]
    
print('\n--- Reporte de Totales por Cliente ---\n')
for cliente, datos in clientes.items():
    print("Cliente :", {cliente})
    print("Cantidad :", datos["cantidad"])
    print("Subtotal: $", datos["subtotal"])
print()
print('\n--- Diccionario de Clientes (Estructura Interna) ---\n',clientes)