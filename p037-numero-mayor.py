# p037-numero-mayor.py
# Encontrar el número mayor entre tres números.
# 11 30 -1

print('\033[2J\033[H')
print('--- Encontrar el número mayor entre tres números.')

print('Dame 3 números enteros separados por espacio:')
n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 >= n2 and n1 >= n3:
    mayor = n1
elif n2 >= n1 and n2 >= n3:
    mayor = n2
else:
    mayor = n3
print(f' El número mayor es {mayor}.')
print('\nProceso terminado.')