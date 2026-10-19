# ====================================================================
# Nombre: Victor Hugo Reyna Leos
# Matrícula: 2630104
# ====================================================================

# ====================================================================
# RESUMEN EJECUTIVO
# Una lista (list) es una colección ordenada y mutable donde podemos
# agregar, quitar o cambiar elementos. Una tupla (tuple) es similar,
# pero es inmutable (no se puede modificar una vez creada). 
# Con la autorización de omitir el tema de diccionarios, este 
# documento cubre exclusivamente los problemas asignados para el 
# manejo de listas (catálogos/compras) y tuplas (coordenadas 2D),
# diseñando sus entradas, salidas, validaciones y casos de prueba.
# ====================================================================

# ====================================================================
# PRINCIPIOS Y BUENAS PRÁCTICAS
# - Usar listas cuando los datos van a estar cambiando (agregar/eliminar).
# - Usar tuplas para proteger datos que son fijos (ej. coordenadas x, y).
# - Evitar modificar una lista mientras la recorres con un for.
# - Escribir código legible nombrando variables en inglés y de forma clara.
# - Validar entradas antes de operar para evitar errores de tipo de dato.
# ====================================================================


# ====================================================================
# Problem 1: Shopping list basics (list operations)
# Descripción: Trabaja con una lista de productos. Crea una lista inicial, 
# permite agregar un producto nuevo al final, muestra el total de 
# elementos y verifica si un producto específico está en la lista.
#
# Entradas:
# - initial_items_text (string)
# - new_item (string)
# - search_item (string)
# Salidas:
# - "Items list:", "Total items:", "Found item: true|false"
# Validaciones:
# - Que las cadenas no estén vacías tras limpiarlas (strip).
#
# Casos de prueba:
# 1) Normal: "apple, banana, orange", "milk", "banana"
# 2) Borde: "apple", "bread", "bread" (busca el recién agregado)
# 3) Error: "   ", "milk", "apple" (texto inicial vacío)
# ====================================================================

def problem_1_shopping_list(initial_items_text, new_item, search_item):
    clean_initial = initial_items_text.strip()
    clean_new = new_item.strip()
    clean_search = search_item.strip()

    if not clean_initial or not clean_new or not clean_search:
        print("Error: invalid input")
        return

    # Crear lista separando por comas y limpiando espacios extra
    items_list = []
    for item in clean_initial.split(","):
        items_list.append(item.strip())

    # Agregar nuevo elemento
    items_list.append(clean_new)

    # Validaciones y búsquedas
    total_items = len(items_list)
    is_in_list = clean_search in items_list

    print(f"Items list: {items_list}")
    print(f"Total items: {total_items}")
    print(f"Found item: {str(is_in_list).lower()}")

print("--- Test Problem 1 ---")
problem_1_shopping_list("apple, banana, orange", "milk", "banana") # Normal
problem_1_shopping_list("apple", "bread", "bread") # Borde
problem_1_shopping_list("   ", "milk", "apple") # Error
print("\n")


# ====================================================================
# Problem 2: Points and distances with tuples
# Descripción: Usa tuplas para representar dos puntos en un plano 2D. 
# Calcula la distancia euclidiana entre ambos y crea una nueva tupla 
# con el punto medio.
#
# Entradas:
# - x1, y1, x2, y2 (float)
# Salidas:
# - "Point A:", "Point B:", "Distance:", "Midpoint:"
# Validaciones:
# - Que las 4 coordenadas se puedan convertir a float.
#
# Casos de prueba:
# 1) Normal: 0, 0, 3, 4 (distancia clásica de 5)
# 2) Borde: 5.5, 5.5, 5.5, 5.5 (mismo punto, distancia 0)
# 3) Error: "uno", 2, 3, 4 (falla al convertir a float)
# ====================================================================

def problem_2_points_distance(x1_input, y1_input, x2_input, y2_input):
    try:
        x1 = float(x1_input)
        y1 = float(y1_input)
        x2 = float(x2_input)
        y2 = float(y2_input)
    except ValueError:
        print("Error: invalid input")
        return

    # Creación de tuplas
    point_a = (x1, y1)
    point_b = (x2, y2)

    # Distancia euclidiana
    distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5

    # Punto medio
    midpoint = ((x1 + x2) / 2.0, (y1 + y2) / 2.0)

    print(f"Point A: {point_a}")
    print(f"Point B: {point_b}")
    print(f"Distance: {round(distance, 2)}")
    print(f"Midpoint: {midpoint}")

print("--- Test Problem 2 ---")
problem_2_points_distance(0, 0, 3, 4) # Normal
problem_2_points_distance(5.5, 5.5, 5.5, 5.5) # Borde
problem_2_points_distance("uno", 2, 3, 4) # Error
print("\n")


# ====================================================================
# CONCLUSIONES
# Esta actividad (enfocada en las primeras dos estructuras) me sirvió 
# para distinguir cuándo poder usar listas y cuándo tuplas. Las listas 
# son bastante flexibles porque permiten métodos como append() para crecer 
# el catálogo de las compras. y las tuplas son
# perfectas para datos que estan juntos y no deben cambiar de valor 
# por error en el código, como las coordenadas X y Y de un punto en 
# un plano geométrico. 
# ====================================================================

# ====================================================================
# REFERENCIAS
# 1) Python documentation - Built-in Types: list, tuple.
# 2) Codecademy: Python Lists and Tuples tutorial.
# 3) freeCodeCamp (español): "Estructuras de datos en Python - Listas".
# 4) Tutorial en YouTube - Canal Fazt (Tema: Manipulación de listas).
# 5) Libro "Python Crash Course" de Eric Matthes (Cap. Estructuras).
# ====================================================================