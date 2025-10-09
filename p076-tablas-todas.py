# p076-tablas-todas.py
#imprime todas las tablas de 1 a n, hasta m
print('')
print ('Imprimiendo las tablas de multiplicar de 1 a n, hasta m')

n=int(input('Hasta que tabla: '))
m=int(input('Hasta que multiplicador: '))
#el bucle exterior se ejecuta n veces
for i in range(1,n+1):
    print(f'\n----- tabla del {i}----')
    #por cada iteracion del bucle exterior, el bucle interior se ejecuta m veces
    for j in range(1, m+1):
        #aqui se ejecutsn las acciones anidadas
        print(f'{i} x {j}= {i*j}')
    print('\n')