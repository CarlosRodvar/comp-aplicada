# p062-conversion-temperaturas.py
# El usuario debe introducir una temperatura inicial y una final en grados Celsius. 
# El programa mostrará la conversión a grados Fahrenheit para cada grado en ese rango, 
# incrementando de uno en uno.

print('\033[H\033[J') 

while True:
    celsius_inicial = int(input("\nIngrese la temperatura inicial en grados Celsius: "))
    celsius_final = int(input("Ingrese la temperatura final en grados Celsius: "))

    if celsius_inicial > celsius_final:
        print("La temperatura inicial debe ser menor o igual a la final.")
        continue

    print(f"\nConversión de {celsius_inicial}°C a {celsius_final}°C a Fahrenheit:")

    celsius = celsius_inicial
    while celsius <= celsius_final:
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C = {fahrenheit:.1f}°F")
        celsius += 1

    if input('\nDeseas continuar (S/N)? ').upper()=='N':
        break

print("\nProceso terminado")
