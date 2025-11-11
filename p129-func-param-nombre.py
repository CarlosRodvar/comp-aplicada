# p129-func-param-nombre.py

def saluda(apaterno: str, amaterno: str, nombre: str, edad:int) -> None:
    print(f'Hola {nombre} {apaterno} {amaterno}, tienes {edad} años')
    print ()


saluda('Lopez', 'Martinez', 'Ana', '25')
saluda(edad=25, nombre='Ana', amaterno='Martinez', apaterno='Lopez')
saluda(nombre='juan', apaterno='Perez', amaterno='Diaz', edad=30)
