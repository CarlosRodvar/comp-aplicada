# p150-dia-semana.py

def obtener_dia_semana(numero):
    """Devuelve el día de la semana según el número (1-7)."""
    dias = {
        1: "Lunes",
        2: "Martes",
        3: "Miércoles",
        4: "Jueves",
        5: "Viernes",
        6: "Sábado",
        7: "Domingo"
    }
    return dias.get(numero) 

numero = int(input("Introduce un número del 1 al 7: "))

dia = obtener_dia_semana(numero)

if dia is None:
    print("Error: El número debe estar entre 1 y 7.")
else:
    print("El día es:", dia)
