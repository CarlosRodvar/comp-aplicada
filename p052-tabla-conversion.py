# p052-tabla-conversion.py
#Muestra una tabla de conversion de Peso a Dollar
tc = 20.71
while True :
    print('\033[H\033[J')
    print("Tabla de Conversion Peso a Dolar")
    print(f'Tipo de Cambio: {tc} Pesos por Dolar')
    print("-"*15)
    while True:
        pi = float(input("Valor inicial: "))
        pf = float(input("Valor final : "))
        if (pi>0 and pf>0) and pi<pf: break       

        print("Error en los valores de entrada, intenta de nuevo")
    c = pi
    print("\nPesos\tDollar")
    print("-"*25)
    while c<=pf :
        print(f'{c:.2f}\t\t{c/tc:.2f}')
        c+=1
    print("-"*25)

    if input('Deseas Continuar(S/N)? ').upper() == 'N':  break

print('\nProceso terminado')