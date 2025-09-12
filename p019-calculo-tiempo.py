 # p019-calculo-tiempo.py
# calcular la conversion de horas a dias, minutos y segundos


horas=int(input('Ingresa las horas:'))
dias = horas//24
minutos = horas * 60
segundos = minutos * 60
print (f'\nEquivalente de {horas} horas:')
print (f'Dias: {dias}')
print (f'minutos: {minutos}')
print (f'segundos: {segundos}')