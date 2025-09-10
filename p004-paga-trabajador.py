# -p004-paga-trabajador.py
# calcula la paga de un trabajador

print ('Calculando la paga de un trabajador \n')

nombre = input ('Nombre :')
horas = int (input ('Horas : ') )
paga = float (input  ('paga por hora: '))


#proceso
tasa =0.03 #impuesto de hacienda
pagabruta= horas* paga
impuesto =pagabruta *tasa
pagoneto =pagabruta -impuesto

#salida
print ('\nResumen de pagos')
print (f'El trabajador {nombre}, trabajó {horas} horas, con una paga de  {paga:.2f} pesos, con una tasa de {tasa:.2%}')
print (f'Paga bruta :{pagabruta:,.2f}')
print (f'Impuesto  :{impuesto:,.2f}')
print (f'Pago neto :{pagoneto:,.2f}')
