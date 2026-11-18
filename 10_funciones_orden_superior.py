# Tema 4.2 Funciones de orden superior
# Una función de orden superior recibe otra función, o devuelve una función.
# map, filter y reduce también lo son. Esas tres están en 12_map_filter_reduce.py.
# Aquí la idea se ve con funciones que tienen nombre.

def duplicar(n):
    return n * 2

def triplicar(n):
    return n * 3

def sumar(a, b):
    return a + b

def multiplicar(a, b):
    return a * b

# Recibe una función y un valor, y aplica esa función al valor.
# Se pasa duplicar, sin paréntesis: queremos la función, no el resultado.
def aplicar(funcion, valor):
    return funcion(valor)

print("aplicar(duplicar, 5):", aplicar(duplicar, 5))
print("aplicar(triplicar, 5):", aplicar(triplicar, 5))

# La operación también llega como argumento. La misma función sirve para sumar o multiplicar.
def operar(a, b, operacion):
    return operacion(a, b)

print("operar con suma:", operar(4, 5, sumar))
print("operar con multiplicación:", operar(4, 5, multiplicar))

# Esta devuelve una función para usarla después.
# Al devolver no van los paréntesis: se entrega la función, no un número.
def elegir_operacion(nombre):
    if nombre == "doble":
        return duplicar
    return triplicar

por_dos = elegir_operacion("doble")
por_tres = elegir_operacion("triple")
print("por_dos(4):", por_dos(4))
print("por_tres(4):", por_tres(4))
