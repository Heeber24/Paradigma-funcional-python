# Tema 4.3 Funciones anónimas
# lambda arma una función de una sola expresión, sin escribir def.
# Sirve cuando la función es corta y casi siempre se va a pasar a otra.
# lambda argumentos: expresión

cuadrado = lambda x: x ** 2
print("Cuadrado de 6 con lambda:", cuadrado(6))

def cuadrado_funcion(x):
    """Calcula el cuadrado de un número."""
    return x ** 2

print("Cuadrado de 6 con def:", cuadrado_funcion(6))

suma = lambda a, b: a + b
print("Suma de 4 y 5 con lambda:", suma(4, 5))

def suma_funcion(a, b):
    """Suma dos números."""
    return a + b

print("Suma de 4 y 5 con def:", suma_funcion(4, 5))

# La lambda cabe en una sola expresión. No lleva varios renglones ni un return escrito.
# Si el cálculo necesita más de un paso, conviene la función con def.
# En 12_map_filter_reduce.py la lambda se usa como argumento de map, filter y reduce.
