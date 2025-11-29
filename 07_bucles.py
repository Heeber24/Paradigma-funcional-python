#Bucles

# Los bucles permiten repetir un bloque de código varias veces mientras se cumpla una condición.
# Bucle 'for' para iterar sobre una secuencia (lista, tupla, cadena, etc.)
print("Bucle for sobre una lista:")
mi_lista = [10, 20, 30, 40, 50]
for elemento in mi_lista:
    print(elemento)

print("Bucle for sobre una tupla:")
mi_tupla = (10, 20, 30, "Hola", 3.14, True)
for valor in mi_tupla:
    print(valor)

print("Bucle for sobre una cadena:")
mi_cadena = "Hola"
for caracter in mi_cadena:
    print(caracter) 


# Bucle 'while' para repetir mientras una condición sea verdadera
print("Bucle while:")
contador = 0
while contador < 5:
    print("Contador:", contador)
    contador += 1  # Incrementar el contador para evitar un bucle infinito


# Uso de 'break' para salir de un bucle
# con for
print("Bucle con break:")
for i in range(10):
    if i == 5:
        print("Se encontró 5, saliendo del bucle.")
        break  # Salir del bucle cuando i es 5
    print(i)

# con while
print("Bucle while con break:")
contador = 0
while True:
    print("Contador:", contador) 
    contador += 1
    if contador >= 3: 
        print("Contador:", contador)
        print("Contador llegó a 3, saliendo del bucle.")
        break  # Salir del bucle cuando el contador llega a 3

# Uso de 'continue' para saltar a la siguiente iteración
print("Bucle con continue:")
for i in range(10):
    if i % 2 == 0:
        continue  # Saltar los números pares
    print(i)  # Imprimir solo números impares

