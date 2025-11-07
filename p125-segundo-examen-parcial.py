# p125-segundo-sxamen-parcial.py
#   Sistema sencillo de captura y procesamiento de inventario para "TecnoTienda".

print ('\033[H\033[J')
print("--- Sistema de Inventario TecnoTienda ---\n")

def formatear_moneda(valor):
    return f"{valor:,.2f}"

def calcular_anchos_columnas(productos):
    # Encabezados de la tabla
    encabezados = {
        "nombre": "Nombre",
        "precio": "Precio",
        "categoria": "Categoría",
        "stock": "Stock",
        "proveedor": "Proveedor",
    }

    # Ancho mínimo: el de los encabezados
    anchos = {k: len(v) for k, v in encabezados.items()}

    # Recorremos los productos para ver el ancho máximo requerido
    for p in productos:
        # Longitud del nombre
        if len(p["nombre"]) > anchos["nombre"]:
            anchos["nombre"] = len(p["nombre"])

        # Precio formateado como texto para medir su longitud
        precio_txt = formatear_moneda(p["precio"])
        if len(precio_txt) > anchos["precio"]:
            anchos["precio"] = len(precio_txt)

        # Categoría
        if len(p["categoria"]) > anchos["categoria"]:
            anchos["categoria"] = len(p["categoria"])

        # Stock (convertido a texto)
        stock_txt = str(p["stock"])
        if len(stock_txt) > anchos["stock"]:
            anchos["stock"] = len(stock_txt)

        # Proveedor
        if len(p["proveedor"]) > anchos["proveedor"]:
            anchos["proveedor"] = len(p["proveedor"])

    return anchos

def imprimir_tabla(productos):
    if len(productos) == 0:
        print("(No hay productos para tabular)")
        return

    anchos = calcular_anchos_columnas(productos)

    # Encabezados
    encabezados = ("Nombre", "Precio", "Categoría", "Stock", "Proveedor")
    print(f"{encabezados[0]:<{anchos['nombre']}} "
          f"{encabezados[1]:>{anchos['precio']}} "
          f"{encabezados[2]:<{anchos['categoria']}} "
          f"{encabezados[3]:>{anchos['stock']}} "
          f"{encabezados[4]:<{anchos['proveedor']}}")

    # Filas
    for p in productos:
        nombre = p["nombre"]
        precio = formatear_moneda(p["precio"])
        categoria = p["categoria"]
        stock = str(p["stock"])
        proveedor = p["proveedor"]

        print(f"{nombre:<{anchos['nombre']}} "
              f"{precio:>{anchos['precio']}} "
              f"{categoria:<{anchos['categoria']}} "
              f"{stock:>{anchos['stock']}} "
              f"{proveedor:<{anchos['proveedor']}}")

def contar_por_campo(productos, campo):
     # Cuenta cuántos productos hay por valor de 'campo' (ej. 'categoria' o 'proveedor').
    
    conteo = {}
    for p in productos:
        clave = p[campo]
        if clave in conteo:
            conteo[clave] += 1
        else:
            conteo[clave] = 1
    return conteo

def imprimir_conteo(titulo, conteos):
    """
    Imprime un bloque de conteos con bullets, por ejemplo:
    Categorías:
    • Laptops: 2
    • Celulares: 1
    """
    print(titulo + ":")
    # Para que la salida sea consistente, los ordenamos alfabéticamente
    llaves = list(conteos.keys())
    llaves.sort()
    for k in llaves:
        print(f"• {k}: {conteos[k]}")

def resumen_inventario(productos):
    """
    Calcula y muestra el resumen del inventario:
      - Total de productos
      - Conteo por categoría
      - Conteo por proveedor
      - Suma y promedio de stock
      - Suma y promedio de precios
      - Producto más caro y más barato
    """
    total = len(productos)
    print(f"Productos totales: {total}")

    if total == 0:
        return

    # Conteos
    por_categoria = contar_por_campo(productos, "categoria")
    por_proveedor = contar_por_campo(productos, "proveedor")

    imprimir_conteo("Categorías", por_categoria)
    imprimir_conteo("Proveedores", por_proveedor)

    # Acumuladores para sumas
    suma_stock = 0
    suma_precios = 0.0

    p_max = productos[0]
    p_min = productos[0]

    for p in productos:
        # Acumulamos stock y precio,  Buscamos el producto con mayor y menor precio
        suma_stock += p["stock"]
        suma_precios += p["precio"]
        if p["precio"] > p_max["precio"]:
            p_max = p
        if p["precio"] < p_min["precio"]:
            p_min = p

    # Promedios
    promedio_stock = suma_stock / total
    promedio_precios = suma_precios / total

    # Impresión con formato
    print(f"Stock -> Suma: {suma_stock:,.0f}, Promedio: {promedio_stock:.2f}")
    print(f"Precio -> Suma: {formatear_moneda(suma_precios)}, "
          f"Promedio: {formatear_moneda(promedio_precios)}")

    print(f"{p_max['nombre']} de {formatear_moneda(p_max['precio'])} es el más caro, "
          f"{p_min['nombre']} de {formatear_moneda(p_min['precio'])} es el más barato.")

def capturar_productos():
    """
    Captura interactiva de productos.
    Repite mientras el usuario no deje el nombre vacío ni escriba '*'.

    Validaciones básicas:
      - precio: número flotante >= 0
      - stock: entero >= 0
      - categoria/proveedor: se pide que no estén vacíos para mayor claridad
    """
    productos = []

    print("TecnoTienda - Sistema de Inventario")
    print("Captura de datos de los productos (* para terminar):")

    while True:
        # --- NOMBRE ---
        nombre = input("Nombre del producto: ").strip()
        
        if nombre == "*":
            break

        # --- PRECIO --- 
        while True:
            precio_txt = input("Precio (ej. 1500.50): ").strip()
            es_valido = True
            try:
                precio = float(precio_txt)
            except:
                es_valido = False
            if es_valido and precio >= 0:
                break
            else:
                print("⚠️  Precio inválido. Intenta de nuevo.")

        # --- CATEGORÍA ---
        categoria = input("Categoría (ej. 'Laptops', 'Celulares', 'Audio'): ").strip()
        while categoria == "":
            print("⚠️  La categoría no puede estar vacía.")
            categoria = input("Categoría (ej. 'Laptops', 'Celulares', 'Audio'): ").strip()

        # --- PROVEEDOR ---
        proveedor = input("Proveedor (ej. 'Sony', 'HP', 'Generico'): ").strip()
        while proveedor == "":
            print("⚠️  El proveedor no puede estar vacío.")
            proveedor = input("Proveedor (ej. 'Sony', 'HP', 'Generico'): ").strip()

        # --- STOCK --- 
        while True:
            stock_txt = input("Stock (ej. 25): ").strip()
            es_valido = True
            # Intentamos convertir a entero
            try:
                stock = int(stock_txt)
            except:
                es_valido = False

            if es_valido and stock >= 0:
                break
            else:
                print("⚠️  Stock inválido. Debe ser un entero >= 0. Intenta de nuevo.")

        # --- ALMACENAR ---
        # Guardamos el producto como diccionario en la lista.
        producto = {
            "nombre": nombre,
            "precio": precio,
            "categoria": categoria,
            "proveedor": proveedor,
            "stock": stock,
        }
        productos.append(producto)

        # Línea en blanco para separar capturas
        print()

    return productos

def imprimir_lista_cruda(productos):
    # Imprime la lista "tal cual" está almacenada.
    print(productos)

def main():
    
    productos = capturar_productos()

    print("\n3.1. DATOS (LISTA DE DICCIONARIOS):\n")
    imprimir_lista_cruda(productos)

    print("\n3.2. TABLA DE DATOS:\n")
    imprimir_tabla(productos)

    print("\n3. RESUMEN:\n")
    resumen_inventario(productos)

if __name__ == "__main__":
    main()
