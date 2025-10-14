# p088-cuadro-hueco-caracter.py
# Imprime un cuadro hueco de caracter deseado
print('\033[H\033[J')
print('Imprime un cuadro hueco de caracter deseado')
lado = int(input("¿Cuántos quieres que mida por lado? "))

c = input("¿Qué carácter quieres? ") 
print("\n--- Cuadro Generado ---")

for i in range(lado):
    for j in range(lado):
        # Primera o última fila → todo con caracteres
        if i == 0 or i == lado - 1:
            print(c, end=" ")
        # En medio → solo los bordes
        else:
            if j == 0 or j == lado - 1:
                print(c, end=" ")
            else:
                print(" ", end=" ")
    print()   
print()
