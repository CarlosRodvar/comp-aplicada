# p005-calculadora-imc.py
#Calcula el indice de masa corporal

print('Calculando el indice de masa corporal (IMC) \n')

#Entrada 
peso_kg = float (input ('Ingresa tu peso en kilogramos :'))
altura_m = float (input('Ingresa tu altura en metros: ') )
imc= peso_kg/(altura_m **2)
print (f'Tu IMC es: {imc:.2f}')

# proceso
imc = peso_kg /(altura_m ** 2) #divide el peso entre la altura al cuadrado (** eleva a la potencia)


#salida
print ("\nEl peso es {0:.2f}kg y la altura es {1:.2f}m y resulta en un IMC de {2:.2f}".format(peso_kg,altura_m, imc))

print(f"\nEl peso es {peso_kg:.2f}kg y la altura es {altura_m:.2f}m y resulta en un IMC de {imc:.2f}")