# p020-numero-suerte.py
# Calcular el numero de la suerte, pidiendo el año de nacimiento y sumando los digitos.


print('Calcular el numero de la suerte\n')
año_nacimiento = int(input('Dame tu año de nacimiento (YYYY): '))
suma_digitos = sum(int(digito) for digito in str(año_nacimiento))

d1 = año_nacimiento // 1000           # primer dígito
d2 = (año_nacimiento // 100) % 10     # segundo dígito
d3 = (año_nacimiento // 10) % 10      # tercer dígito
d4 = año_nacimiento % 10              # cuarto dígito

print("\nDígitos individuales:")
print(d1)
print(d2)
print(d3)
print(d4)

print(f'Tu numero de la suerte es: {suma_digitos}') 

