# p056-contador-vocales.py
# Cuenta las vocales y consonantes en una frase y otros caracteres


while True:
    print('\033[H\033[J')
    print("Contador de Vocales y Consonantes")
    frase = input("\nIntroduce una frase: ").lower()
    print (len(frase))
    vocales=consonantes=otros=0
    indice = 0
    while indice < len(frase):
        caracter = frase[indice] #tomamos rl caracter correspondiente

        if 'a' <= caracter <= 'z': #vwrifiamos que sea letra
            if caracter in "aeiou":
                vocales += 1
            else: #es constante
                consonantes += 1

        else: #es cualquiero otra cosa

            otros += 1

    indice += 1 #me paso al siguiente caracter
    print(f"\nAnálisis de la frase:")
    print(f"Número de vocales: {vocales}")
    print(f"Número de consonantes: {consonantes}")
    print(f"Número de caracteres no alfabéticos: {otros}")
    if input('\n¿Deseas analizar otra frase (S/N)? ').upper() == 'N': break

print("\nProceso terminado")