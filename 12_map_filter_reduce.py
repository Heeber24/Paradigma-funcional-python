# Tema 4.4 Herramientas funcionales: map, filter, reduce
# Las tres reciben una función, por eso son de orden superior.
# map y filter devuelven un iterable. list() lo convierte en lista para poder verlo.
# La lista original no se modifica: el resultado es una lista nueva.

numeros = [1, 2, 3, 4, 5]

# map aplica una función a cada elemento
cuadrados = list(map(lambda x: x ** 2, numeros))
print("Cuadrados con lambda:", cuadrados)

def elevar_al_cuadrado(x):
    """Eleva un número al cuadrado."""
    return x ** 2

cuadrados_con_def = list(map(elevar_al_cuadrado, numeros))
print("Cuadrados con def:", cuadrados_con_def)
print("Lista original:", numeros)

# filter se queda con los elementos donde la función devuelve True
numeros_pares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros_pares))
print("Pares con lambda:", pares)

def es_par(x):
    """Devuelve True si el número es par."""
    return x % 2 == 0

pares_con_def = list(filter(es_par, numeros_pares))
print("Pares con def:", pares_con_def)

# reduce pliega la lista hasta dejar un solo valor.
# Hay que importarla de functools.
# Con [1, 2, 3, 4, 5] va así: 1 + 2 = 3, 3 + 3 = 6, 6 + 4 = 10, 10 + 5 = 15.
# x es lo acumulado y y es el siguiente número.
from functools import reduce

suma_total = reduce(lambda x, y: x + y, numeros)
print("Suma con lambda:", suma_total)

def sumar(x, y):
    """Suma dos números."""
    return x + y

suma_con_def = reduce(sumar, numeros)
print("Suma con def:", suma_con_def)

# Las tres se pueden encadenar: primero filter, luego map y al final reduce.
# Ese recorrido está en Ejercicio_03.py.
