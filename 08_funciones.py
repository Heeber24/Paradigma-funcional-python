# Funciones en Python

# Definición de una función simple
def saludar(nombre):
    """Función que saluda a una persona por su nombre."""
    saludo = f"Hola, {nombre}!" # Formateo de cadena usando f-string
    return saludo
# Llamada a la función
mensaje = saludar("Ana")
print(mensaje)

# Función con múltiples parámetros
def sumar(a, b):
    """Función que suma dos números."""
    return a + b
resultado = sumar(5, 10)
print("Suma:", resultado)  

# Función con valor por defecto en un parámetro
def potencia(base, exponente=2):        
    """Función que calcula la potencia de un número."""
    return base ** exponente
resultado_potencia = potencia(3)  # Usa el valor por defecto del exponente
print("Potencia con exponente por defecto (3^2):", resultado_potencia)
resultado_potencia_custom = potencia(2, 3)  # Especifica el exponente
print("Potencia con exponente personalizado (2^3):", resultado_potencia_custom)


# Función con número variable de argumentos
def lista_elementos(*elementos): # * indica que la función puede recibir un número variable de argumentos es como un apuntador a una tupla o lista
    """Función que recibe un número variable de nombres y los imprime."""
    for elementos in elementos:
        print("Nombre:", elementos)
lista_elementos("Juan", "María", "Pedro", 23, True) # Se pueden pasar diferentes tipos de datos

# Función con argumentos nombrados
def informacion_personal(nombre, edad, ciudad):
    """Función que muestra la información personal de una persona."""
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")
informacion_personal(edad=30, ciudad="Madrid", nombre="Lucía")

# Función lambda (función anónima) estas funciones son útiles para operaciones simples y se definen en una sola línea
# Ejemplo de función lambda para calcular el cuadrado de un número
# lambda argumentos: expresión
cuadrado = lambda x: x ** 2 
print("Cuadrado de 6 usando función lambda:", cuadrado(6))

# Sin función lambda
def cuadrado_funcion(x):
    """Función que calcula el cuadrado de un número."""
    return x ** 2
print("Cuadrado de 6 usando función normal:", cuadrado_funcion(6))


# Otro ejemplo de función lambda para sumar dos números
suma = lambda a, b: a + b
print("Suma de 4 y 5 usando función lambda:", suma(4, 5))

# Sin función lambda
def suma_funcion(a, b):
    """Función que suma dos números."""
    return a + b
print("Suma de 4 y 5 usando función normal:", suma_funcion(4, 5))   

# La estructura de una funcion lambda es:
# lambda argumentos: expresión
# Las funciones lambda son útiles cuando se necesitan funciones pequeñas y rápidas sin la necesidad de definir una función completa con 'def'.
# Sin embargo, para funciones más complejas o que requieran múltiples líneas de código, es mejor usar la definición tradicional con 'def'.
# Ejemplo de uso de función lambda con funciones integradas como 'map' y 'filter'
# Usando 'map' para aplicar una función lambda a cada elemento de una lista

