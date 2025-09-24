# p035-tipo-triangulo.py
# Objetivo: Clasificar un triángulo según la longitud de sus tres lados.
#Lados iguales equilatero, dos lados iguales isoceles, ningun lado igual escaleno

print ('\033[2J\033[H')
print("--- CLASIFICADOR DE TRIÁNGULOS ")
print("Ingresa la longitud de los tres lados de un triángulo.")


lado_a = float(input("Lado a: "))
lado_b = float(input("Lado b: "))
lado_c = float(input("Lado c: "))

if lado_a == lado_b and lado_b == lado_c:
    print(f" Es un triángulo EQUILÁTERO (todos los lados son iguales).")
elif lado_a == lado_b or lado_a == lado_c or lado_b == lado_c:
    print(f" Es un triángulo ISÓSCELES (al menos dos lados son iguales).")
else:
    print(f" Es un triángulo ESCALENO (ningún lado es igual).")

print("\nProceso terminado.")