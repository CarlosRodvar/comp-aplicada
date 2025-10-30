# p120-contar-caracteres.py
# Pedir al usuario una cadena
cadena = input("Ingresa una cadena de texto: ")

frecuencias = {}


for caracter in cadena:
    if caracter in frecuencias:
        frecuencias[caracter] += 1
    else:
        frecuencias[caracter] = 1
print("Frecuencia de caracteres:")
print(frecuencias)
