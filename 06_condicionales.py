# Condicionales

# Las condicionales en Python permiten ejecutar bloques de código basados en ciertas condiciones.

# Condicional if, elif y else
# Estructura básica de una condicional if
edad = 18
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")

# Estructura con elif para múltiples condiciones
nota = 85
if nota >= 90:
    print("Excelente")
elif nota >= 75:
    print("Bueno")
elif nota >= 60:
    print("Suficiente")
else:
    print("Insuficiente")

# Condicionales anidadas, se usan para verificar múltiples niveles de condiciones, por ejemplo: saber si un número es positivo y par o impar
numero = 10
if numero > 0:
    if numero % 2 == 0:
        print("El número es positivo y par.")
    else:
        print("El número es positivo e impar.") 
else:
    print("El número es negativo o cero.")

# Otra forma de saber si un número es positivo y par o impar es uniendo las dos condiciones 
num = 10
if num > 0 and num % 2 == 0:
    print("El número es positivo y par.")
elif num > 0 and num % 2 != 0:
    print("El número es positivo e impar.") 
else:
    print("El número es negativo o cero.")

# Las operaciones lógicas también se pueden usar en condicionales
a = True
b = False
if a and not b: # not b es lo mismo que b == False
    print("a es True y b es False")
if a or b:
    print("Al menos una de las variables es True")

# Ejemplo de uso de condicionales con listas
mi_lista = [10, 15, 20, 25, 30] 
valor_buscar = 20
if valor_buscar in mi_lista:
    print(f"El valor {valor_buscar} se encuentra en la lista.")
else:
    print(f"El valor {valor_buscar} no se encuentra en la lista.")

# Ejemplo de uso de condicionales con cadenas de texto
mi_cadena = "Hola, bienvenido a Python"
if "Python" in mi_cadena:
    print("La cadena contiene la palabra 'Python'.")
else:
    print("La cadena no contiene la palabra 'Python'.") 

# Ejemplo de uso de condicionales con tuplas
mi_tupla = (10, 20, 30, "Hola", 3.14, True)
valor_tupla = "Hola"
if valor_tupla in mi_tupla:
    print(f"El valor '{valor_tupla}' se encuentra en la tupla.")
else:
    print(f"El valor '{valor_tupla}' no se encuentra en la tupla.")

# Un diccionario guarda pares clave-valor. La clave sirve para buscar el valor.
# Se escribe entre llaves: {"nombre": "Ana", "edad": 25}
# Aquí lo usamos para ver el if. Con in se pregunta si la clave existe.
mi_diccionario = {"a": 1, "b": 2, "c": 3}
clave_buscar = "b"
if clave_buscar in mi_diccionario:

    print(f"La clave '{clave_buscar}' se encuentra en el diccionario con valor {mi_diccionario[clave_buscar]}.")
else:   
    print(f"La clave '{clave_buscar}' no se encuentra en el diccionario.")

