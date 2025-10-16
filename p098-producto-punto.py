# p098-producto-punto.py
# # Cálculo del producto punto de dos vectores
# Vectores representados como listas

print('\033[H\033[J')
print("--- Cálculo del Producto Punto ---\n")

a = [1, 3, -5]
b = [4, -2, -1]
producto_punto = []
print(f"Vector A: {a}")
print(f"Vector B: {b}\n")
if len(a) == len(b):
    for i in range(len(a)):
        producto = a[i] * b[i]
        producto_punto += producto
        print(f'Vector C: {producto_punto}')
        print(f"El producto punto es: {sum(producto_punto)}")
    else:
        print("Error: Los vectores deben tener la misma longitud para calcular el producto punto.")
