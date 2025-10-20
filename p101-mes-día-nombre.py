#p101-mes-día-nombre.py
#  
print('\033[H\033[J')

# Listas predefinidas
nombres_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                 "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
dias_meses = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# Leer número de mes
while True:
    mes = int(input("Introduzca un número de mes (1-12): "))

    if mes < 1 or mes > 12:
        print("❌ Error: el número debe estar entre 1 y 12.")
    else:
        break

# Mostrar resultados
print("\n--- Resultados ---")
print("Mes:", nombres_meses[mes - 1])
print("Días:", dias_meses[mes - 1])
