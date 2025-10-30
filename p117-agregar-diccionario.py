# p117-agregar-diccionario.py
# crear y agregar elementos a un diccionario

print ('\033[H\033[J')
print ('Agregar Elementos a Diccionario\n')

ventas = {
    'Juan': 1550,
    'Jose': 2600,
    'Maria': 2220
}

print("Diccionario inicial:")
print(ventas)


ventas['Rocio'] = 2500  
ventas['Mateo'] = 1567    
ventas.update({'Andrea': 9567})  
ventas.update({'Miguel': 1234})  

print("Diccionario actualizado:")
print(ventas)