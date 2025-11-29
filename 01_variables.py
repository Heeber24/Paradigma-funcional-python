### Hola Mundo ###
a="Soy una variable" # Tipo 'str'
b=5 # Tipo 'int'
c=1.5 # Tipo 'float'
d=True # Tipo 'bool'
e=3 + 1j # Tipo 'complex' la j representa la parte imaginaria 

# Imprimir las variables 
print(a)
print(b)
print(c)
print(d)
print(e)

# Imprimir variables con su tipo de dato
print(type("Soy una variable"))  
print(type(5)) 
print(type(1.5))  
print(type(True)) 
print(type(3 + 1j))  

# Podemos reasignar valores a las variables
a = "Ahora soy otra variable"
b = 10
c = 2.5
d = False
e = 4 + 2j
#otra forma de imprimir todas las variables en una sola línea
print(a, b, c, d, e)

#No hay que declarar el tipo de variable, Python lo detecta automáticamente
#No es necesario usar punto y coma al final de cada línea
#Los nombres de las variables son sensibles a mayúsculas y minúsculas
#No se pueden usar palabras reservadas de Python como nombres de variables    
#No se pueden usar espacios en los nombres de las variables
#Ejemplos de nombres de variables válidos
mi_variable = 10
otraVariable = 20 # estilo camelCase 
_variable3 = 30

#Ejemplos de nombres de variables inválidos (descomentar para ver errores)
# 2variable = 10 # No puede comenzar con un número
# mi variable = 20 # No puede contener espacios
# def = 30 # No puede usar palabras reservadas


#no hay constantes en Python, pero por convención se usan nombres en mayúsculas para indicar que no deben cambiarse
PI = 3.1416
GRAVEDAD = 9.81
print("Constantes:", PI, GRAVEDAD)