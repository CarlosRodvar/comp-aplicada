"""
Objetivo: Programa para administrar la venta de boletos
Nombre del Alumno: Carlos Abraham Rodriguez Vargas
Matrícula: [Escribe tu matrícula aquí]
Materia: Computación Aplicada
Examen: Primer Parcial
"""

# --- Inicialización de Contadores y Acumuladores ---
# Aquí se declaran todas las variables que necesitarás para guardar los datos
ventas=0
# --- Contadores de Asistentes ---
total_estudiantes = 0
total_adultos = 0
total_tercera = 0
total_academicos = 0

# ... (agrega los demás contadores de tipo de comprador y de sexo)
total_asistentes = 0
total_rechazados = 0
total_hombres = 0
total_mujeres = 0
suma_edades = 0

# --- Acumuladores de Ingresos ---
ingresos_estudiantes = 0.0
ingresos_adultos = 0.0
ingresos_tercera = 0.0
ingresos_academicos = 0.0

# ... (agrega los demás acumuladores de ingresos)
ingresos_totales = 0.0


# --- Precios de los Boletos (constantes) ---
PRECIO_ESTUDIANTE = 50.0
PRECIO_ADULTO = 90.0
PRECIO_TERCERA = 60.0
PRECIO_ACADEMICO = 70.0
# ... (agrega las demás constantes de precios)

print('\033[2J\033[H')
print("--- Sistema de Venta de Boletos de Cine ---")

# --- Ciclo Principal para la Venta de Boletos ---
# Usaremos un ciclo while para registrar ventas hasta que el usuario decida parar.
continuar_venta = "s"
while continuar_venta == "s":
    ventas+=1
    print(f"\n--- VENTA {ventas} ---")
    
    # --- 1. Solicitud de Datos ---
    # Pide la edad, el tipo de comprador y el sexo.
    # ¡Recuerda convertir la edad a un número entero!
    
    edad = int(input("Introduce la edad del comprador: "))
    # ... (pide el tipo de comprador y el sexo)
    
    if edad<=13:
        print('❌ACCESO DENEGADO❌: El comprador es menor de 13 años.')
        total_rechazados += 1  
        continue
       
    # --- 2. Validación de Edad (Clasificación B) ---
    # La película es para mayores de 13 años.
    
    else: 
        print('----------------------------------')
        print("\nTipo de comprador:")
        print("1. Estudiante ($50)") 
        print("2. Adulto ($90)")
        print("3. Tercera Edad ($60)")
        print("4. Académico ($70)")
        tipo_comprador = input("Selecciona el tipo de comprador (E/A/T/Ac): ").upper()
        print('----------------------------------')
        sexo = input("Introduce el sexo del comprador (H/M): ").lower()
        print('----------------------------------')
        if tipo_comprador == "E":
            tipo_texto = "Estudiante"
        elif tipo_comprador == "A":
            tipo_texto = "Adulto"
        elif tipo_comprador == "T":
            tipo_texto = "Tercera edad"
        elif tipo_comprador == "Ac":
            tipo_texto = "Academico"
        # Si la edad es permitida, procede con la venta.
        # Muestra el mensaje de bienvenida con los datos registrados
        
        print(f"¡Bienvenido(a)! Datos registrados -> {edad} años, Sexo: {'Hombre' if sexo=='h' else 'Mujer'}, Tipo: {tipo_texto}.")
        
        # --- 3. Actualización de Estadísticas Generales ---
        # Incrementa el contador de asistentes y suma la edad para el promedio.
        # Incrementa el contador de sexo correspondiente (hombre o mujer).
        total_asistentes += 1
        suma_edades += edad
        if sexo == "h":
            total_hombres += 1
        elif sexo == "m":
            total_mujeres += 1
        # --- 4. Cálculo de Costo y Actualización de Contadores Específicos ---
        # Usa una estructura if/elif/else para determinar el precio y actualizar
        # los contadores del tipo de comprador y sus ingresos.
        # Suma el costo del boleto a los ingresos totales.
        if tipo_comprador == 'E':
            tipo_texto='Estudiante'
            total_estudiantes += 1
            ingresos_estudiantes += PRECIO_ESTUDIANTE
            ingresos_totales += PRECIO_ESTUDIANTE
            print(f"El costo del boleto es: ${PRECIO_ESTUDIANTE:.2f}")
        elif tipo_comprador == 'A':
            total_adultos += 1
            ingresos_adultos += PRECIO_ADULTO
            ingresos_totales += PRECIO_ADULTO
            print(f"El costo del boleto es: ${PRECIO_ADULTO:.2f}")
        elif tipo_comprador == 'T':
            total_tercera += 1
            ingresos_tercera += PRECIO_TERCERA
            ingresos_totales += PRECIO_TERCERA
            print(f"El costo del boleto es: ${PRECIO_TERCERA:.2f}")
        elif tipo_comprador == 'Ac':
            total_academicos += 1
            ingresos_academicos += PRECIO_ACADEMICO
            ingresos_totales += PRECIO_ACADEMICO
            print(f"El costo del boleto es: ${PRECIO_ACADEMICO:.2f}")
        else:
            print("⚠️Tipo de comprador no válido. Venta cancelada.⚠️")
            total_asistentes -= 1  # Revertir el conteo de asistentes
            suma_edades -= edad  # Revertir la suma de edades
            continue  # Salta al inicio del ciclo para una nueva venta
        # Si la edad no es permitida, muestra un mensaje y actualiza el contador ()

        # ... (incrementa el contador de personas rechazadas)

    # Pregunta al usuario si desea registrar otra venta.
    continuar_venta = input("\n¿Deseas registrar otra venta? (S/N): ").lower()

# --- FIN DEL CICLO ---

# --- 5. Cálculo de Promedio ---
# Calcula el promedio de edad. Cuidado con la división entre cero si no hubo asistentes.
promedio_edad = 0

# if total_asistentes > 0:
#     promedio_edad = ... # (calcula el promedio aquí)
promedio_edad = suma_edades / total_asistentes if total_asistentes > 0 else 0

# --- 6. Impresión del Reporte Final ---
print("\n*** REPORTE FINAL DE LA FUNCIÓN ***")

print("\n--- Estadísticas del Público ---")
# Imprime todos los totales de asistentes por tipo y sexo.
print(f"Total Estudiantes: {total_estudiantes}")
print(f'Total Adultos: {total_adultos}')
print(f"Total Tercera Edad: {total_tercera}")
print(f"Total Académicos: {total_academicos}")
print('----------------------------------')
print(f"Total Hombres: {total_hombres}")
print(f"Total Mujeres: {total_mujeres}")
print('----------------------------------')
print(f"Total Asistentes: {total_asistentes}")
print(f"Promedio de edad: {promedio_edad:.2f}")
print(f"Total Rechazados (menores de 13 años): {total_rechazados}")


print("\n--- 💰 Reporte de Ingresos 💰 ---")
# Imprime todos los ingresos por tipo de comprador y el total general.
# Utiliza formato para mostrar dos decimales en el dinero.
print(f"Ingresos Estudiantes: ${ingresos_estudiantes:.2f}")
print(f"Ingresos Adultos: ${ingresos_adultos:.2f}")
print(f"Ingresos Tercera Edad: ${ingresos_tercera:.2f}")
print(f"Ingresos Académicos: ${ingresos_academicos:.2f}")
print('----------------------------------')
print(f" INGRESOS TOTALES: ${ingresos_totales:.2f}")


print("\n--- Rentabilidad ---")
# --- 7. Mensaje de Rentabilidad ---
# Usa una estructura if/elif/else para determinar si las ganancias
# fueron BAJAS, MODERADAS o BUENAS, basándote en los ingresos totales.
if ingresos_totales < 1500:
    print("La función generó BAJAS ganancias.")
elif ingresos_totales <= 3500:
    print("La función generó GANANCIAS MODERADAS.")
else:
    print("La función generó BUENAS ganancias.")

print("\n✅ Proceso terminado.✅")

"""
Preguntas: Explica con tus palabras

1. Imagina que el cine decide implementar una promoción: los martes, todos los boletos de Adulto tendrán un 20% de descuento. 
¿Qué cambios tendrías que hacer en tu código para agregar esta funcionalidad? 
Menciona qué nueva pregunta le harías al usuario y en qué parte del código agregarías la nueva lógica.

[Necesitamos saber si el dia de la funcion es martes, entonces agregaria algo como: dia=input('Hoy es martes?(S/N):').lower' 
ahora en la eleccion del tipo de comprador debe agregar un if si es que es en un martes, y luego se agrega el descuento (precio*0.8)]

2. Supongamos que, al probar tu programa, el "Total Recaudado en General" siempre te da un resultado incorrecto, 
aunque los ingresos por cada tipo de comprador parecen correctos. 
Describe, paso a paso, qué harías para encontrar el error. 
¿En qué líneas específicas de tu código pondrías atención para verificar los valores y solucionar el problema?

[Primero se hacen pruebas pequeñas de donde podamos calcular manualmente. Despues te vas al designador ingresos totales
de cada opcion de tipo de comprador y busca si se asigna o se acumula. por ejemplo en este codigo las lineas 108,113,118,123]
"""