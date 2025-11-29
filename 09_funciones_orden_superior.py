# Funciones de orden superior
# Las funciones de orden superior son aquellas que pueden tomar otras funciones como argumentos o devolver funciones como resultados.
# map, filter y reduce son ejemplos comunes de funciones de orden superior en Python.

# map sirve para aplicar una función a cada elemento de un iterable (como una lista) y devolver un nuevo iterable con los resultados
# argumentos: expresión
numeros = [1, 2, 3, 4, 5] 
cuadrados = list(map(lambda x: x ** 2, numeros)) # x es cada elemento de la lista numeros 
print("Cuadrados de la lista de números:", cuadrados)

# Sin función lambda
def elevar_al_cuadrado(x):
    """Función que eleva un número al cuadrado."""
    return x ** 2
cuadrados_sin_lambda = list(map(elevar_al_cuadrado, numeros))
print("Cuadrados de la lista de números sin lambda:", cuadrados_sin_lambda)


# filter sirve para filtrar elementos de un iterable basándose en una función que devuelve True o False
# argumentos: expresión
numeros_pares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = list(filter(lambda x: x % 2 == 0, numeros_pares)) # Filtra los números pares
print("Números pares de la lista:", pares)

# Sin función lambda
def es_par(x):
    """Función que verifica si un número es par."""
    return x % 2 == 0

pares_sin_lambda = list(filter(es_par, numeros_pares))
print("Números pares de la lista sin lambda:", pares_sin_lambda)


# reduce sirve para reducir un iterable a un solo valor aplicando una función acumulativa
# para usar reduce es necesario importar la función desde el módulo functools
from functools import reduce

numeros_reducir = [1, 2, 3, 4, 5]
suma_total = reduce(lambda x, y: x + y, numeros_reducir) # x es el acumulador y es el siguiente elemento de la lista
print("Suma total de la lista usando reduce:", suma_total)

# Sin función lambda
def sumar(x, y):
    """Función que suma dos números."""
    return x + y
suma_total_sin_lambda = reduce(sumar, numeros_reducir)
print("Suma total de la lista sin lambda usando reduce:", suma_total_sin_lambda)
