# Tema 4.1 Características funcionales de Python
# Python no es un lenguaje solo funcional, pero sí deja programar en ese estilo.
# La pieza clave es que una función se trata como cualquier otro valor:
# se puede guardar en una variable y usarse después.

def duplicar(n):
    return n * 2

def triplicar(n):
    return n * 3

# Sin paréntesis no se ejecuta: operacion guarda la función duplicar
operacion = duplicar
print("Resultado de operacion(5):", operacion(5))

# También se pueden guardar varias funciones en una lista y usarlas una por una
operaciones = [duplicar, triplicar]
print("Funciones guardadas en una lista:")
for funcion in operaciones:
    print(funcion(4))

# Una función pura solo calcula y devuelve.
# Con los mismos datos de entrada, el resultado es el mismo.
def sumar(a, b):
    return a + b

print("Suma:", sumar(2, 3))
print("Suma otra vez:", sumar(2, 3))

# Esta otra hace algo más: imprime y modifica la lista que recibió.
def agregar_numero(lista, numero):
    print("Agregando", numero)
    lista.append(numero)

numeros = [1, 2]
agregar_numero(numeros, 3)
print("Lista después de agregar:", numeros)

# Las cadenas no se modifican. upper() crea otra cadena y la original sigue igual.
texto = "hola"
texto_nuevo = texto.upper()
print("Texto original:", texto)
print("Texto nuevo:", texto_nuevo)

# Con las tuplas pasa lo mismo. Esto ya se vio en 05_tuplas.py.
# punto[0] = 9  # esto marca error: la tupla no se puede cambiar
punto = (1, 2)
otro_punto = punto + (3,)
print("Tupla original:", punto)
print("Tupla nueva:", otro_punto)

# Las listas sí se pueden modificar, como en 04_listas.py.
# En el estilo funcional se prefiere crear un valor nuevo y dejar el original quieto.
