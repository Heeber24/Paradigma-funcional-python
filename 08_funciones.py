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
# El * junta en una tupla todos los valores que lleguen, sin pedirlos uno por uno
def lista_elementos(*elementos):
    """Recibe varios datos, los junta en una tupla y los imprime uno por uno."""
    for elemento in elementos:
        print("Elemento:", elemento)
lista_elementos("Juan", "María", "Pedro", 23, True) # Se pueden pasar diferentes tipos de datos

# Función con argumentos nombrados
def informacion_personal(nombre, edad, ciudad):
    """Función que muestra la información personal de una persona."""
    print(f"Nombre: {nombre}, Edad: {edad}, Ciudad: {ciudad}")
informacion_personal(edad=30, ciudad="Madrid", nombre="Lucía")

# Las funciones anónimas (lambda) están en 11_funciones_anonimas.py
# Pasar una función a otra está en 10_funciones_orden_superior.py

