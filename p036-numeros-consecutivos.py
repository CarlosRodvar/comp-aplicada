# p036-numeros-consecutivos.py
# Verificar si 3 números son consecutivos
# 9 10 11   1 4 6    


print('\033[2J\033[H')
print('--- Verificar si 3 números son consecutivos')
print('Dame 3 números enteros separados por espacio:')

n1, n2, n3 = input().split()
n1, n2, n3 = int(n1), int(n2), int(n3)

if n1 + 1 == n2 and n2 + 1 == n3:
    print(f' {n1}, {n2}, {n3} son consecutivos !')   
else : 
    print(f' {n1}, {n2}, {n3} no son consecutivos !')
print('\nProceso terminado.')



