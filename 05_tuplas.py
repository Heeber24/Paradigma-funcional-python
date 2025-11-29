#Tuplas 

#Una tupla es una estructura de datos que permite almacenar una colección ordenada e inmutable de elementos.
#Las tuplas se definen utilizando paréntesis () y los elementos se separan por comas.
#Crear una tupla
mi_tupla = (10, 20, 30, "Hola", 3.14, True)
print("Tupla completa:", mi_tupla)

#Acceder a elementos de una tupla mediante índices
print("Primer elemento:", mi_tupla[0])  # Accede al primer elemento
print("Último elemento:", mi_tupla[-1])  # Accede al último elemento

#Las tuplas son inmutables, no se pueden modificar sus elementos después de la creación
#mi_tupla[1] = 25  # Esto generará un error
#Sin embargo, se pueden realizar operaciones que generen nuevas tuplas
#Concatenación de tuplas
otra_tupla = (40, 50)       
tupla_concatenada = mi_tupla + otra_tupla
print("Tupla concatenada:", tupla_concatenada)  

#Repetición de tuplas
tupla_repetida = mi_tupla * 2
print("Tupla repetida:", tupla_repetida)

#Longitud de una tupla
longitud = len(mi_tupla)
print("Longitud de la tupla:", longitud)

#Slicing (subtuplas)
subtupla = mi_tupla[1:4]  # Elementos desde el índice 1 hasta el 3
print("Subtupla (índices 1 a 3):", subtupla)

#Desempaquetado de tuplas
a, b, c, d, e, f = mi_tupla
print("Desempaquetado:")
print("a:", a)
print("b:", b)
print("c:", c)
print("d:", d)
print("e:", e)
print("f:", f)

#Métodos comunes de tuplas
contador = mi_tupla.count(10)  # Cuenta cuántas veces aparece el elemento 10
indice = mi_tupla.index("Hola")  # Devuelve el índice del primer elemento
print("El elemento 10 aparece", contador, "veces en la tupla.")
print("El índice de 'Hola' en la tupla es:", indice)

