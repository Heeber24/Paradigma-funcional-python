#Listas 

# Definición de una lista
mi_lista = [10, 20, 30, 40, 50]
print("Lista original:", mi_lista)

# Acceso a elementos por índice (comienza en 0)
primer_elemento = mi_lista[0]
ultimo_elemento = mi_lista[-1] # Acceso al último elemento usando índice negativo
print("Primer elemento:", primer_elemento)
print("Último elemento:", ultimo_elemento)

# Modificación de elementos
mi_lista[2] = 35  # Cambia el tercer elemento (índice 2) a 35
print("Lista después de modificación:", mi_lista)

# Agregar elementos al final de la lista
mi_lista.append(60)
print("Lista después de append:", mi_lista)

# Insertar elementos en una posición específica
mi_lista.insert(1, 15) # Inserta 15 en el índice 1
print("Lista después de insert:", mi_lista)

# Eliminar elementos por valor
mi_lista.remove(40) # Elimina el primer elemento con valor 40
print("Lista después de remove:", mi_lista)

# Eliminar elementos por índice
elemento_eliminado = mi_lista.pop(3) # Elimina el elemento en el índice 3
print("Elemento eliminado con pop:", elemento_eliminado)
print("Lista después de pop:", mi_lista)

# Longitud de la lista
longitud = len(mi_lista)
print("Longitud de la lista:", longitud)

# Slicing (sublistas)
sublista = mi_lista[1:4]  # Elementos desde el índice 1 hasta el 3
print("Sublista (índices 1 a 3):", sublista)

# Recorrer la lista, elemento por elemento. El bucle for se explica en 07_bucles.py
print("Elementos de la lista:")
for elemento in mi_lista:
    print(elemento)

# Métodos comunes de listas
mi_lista.sort()  # Ordena la lista en orden ascendente
print("Lista ordenada:", mi_lista)

mi_lista.reverse()  # Invierte el orden de la lista
print("Lista invertida:", mi_lista)

# Comprobación de pertenencia
existe_20 = 20 in mi_lista
existe_100 = 100 in mi_lista
print("¿Existe 20 en la lista?", existe_20)
print("¿Existe 100 en la lista?", existe_100)

# Copiar una lista  
copia_lista = mi_lista.copy() # Crear una copia de la lista igual se puede usar copia_lista = list(mi_lista)
print("Copia de la lista:", copia_lista)

# Limpiar todos los elementos de la lista
mi_lista.clear()
print("Lista después de clear:", mi_lista)

# Crear una lista vacía y agregar elementos posteriormente
otra_lista = []
otra_lista.append("Python")
otra_lista.append("es")
otra_lista.append("genial")
print("Otra lista:", otra_lista)

# Concatenar listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
lista_concatenada = lista1 + lista2
print("Lista concatenada:", lista_concatenada)

# Repetir listas    
lista_repetida = lista1 * 3
print("Lista repetida:", lista_repetida)  

# Contar ocurrencias de un elemento
lista_ejemplo = [1, 2, 2, 3, 4, 2, 5]
conteo_dos = lista_ejemplo.count(2)
print("Número de ocurrencias de 2 en lista_ejemplo:", conteo_dos)

# Encontrar el índice de un elemento
indice_tres = lista_ejemplo.index(3)
print("Índice del primer 3 en lista_ejemplo:", indice_tres)

# Extender una lista con otra lista
lista_ejemplo.extend([6, 7, 8])
print("Lista después de extend:", lista_ejemplo)

# Convertir una cadena en una lista de caracteres
cadena = "Hola"
lista_caracteres = list(cadena)
print("Lista de caracteres de la cadena 'Hola':", lista_caracteres)

# Convertir una lista de caracteres en una cadena
cadena_desde_lista = ''.join(lista_caracteres)
print("Cadena desde lista de caracteres:", cadena_desde_lista)

