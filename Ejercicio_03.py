# Este es el ejercicio más completo, ya que te exige combinar las tres Funciones de Orden Superior (filter, map, reduce) de forma secuencial para resolver un problema de cálculo.

# Dada una lista de tuplas que representan los ítems de un carrito de compras con el formato (nombre_producto, precio_unitario, cantidad_en_stock).
# 1. Filtra (filter): Utiliza filter con una lambda para seleccionar solo los productos cuya cantidad en stock sea mayor que 5.
# 2. Mapea (map): Utiliza map con una lambda sobre el resultado del filtro para calcular el valor total de inventario de cada producto seleccionado (precio_unitario * cantidad_en_stock).
# 3. Reduce (reduce): Utiliza reduce con una lambda para obtener la suma total de los valores de inventario calculados en el paso anterior.

# Datos de inicio
# from functools import reduce
# # (nombre_producto, precio_unitario, cantidad_en_stock)
# inventario = [
#     ("Libro", 15.00, 10),  # Debe incluirse (15.00 * 10 = 150.0)
#     ("Pluma", 2.50, 4),    # Debe excluirse (stock <= 5)
#     ("Mochila", 45.00, 7), # Debe incluirse (45.00 * 7 = 315.0)
#     ("Lápiz", 1.00, 20),   # Debe incluirse (1.00 * 20 = 20.0)
# ]

# Tarea a realizar
# Escribe el código que ejecute los tres pasos secuenciales para obtener un único valor que represente el valor total del inventario de los productos con más de 5 unidades en stock.

# Resultado esperado
# Productos filtrados: [('Libro', 15.0, 10), ('Mochila', 45.0, 7), ('Lápiz', 1.0, 20)]
# Valores individuales (map): [150.0, 315.0, 20.0]
# Valor Total del Inventario: 485.0

