#Cadenas

# Definición de cadenas
cadena1 = "Hola, Mundo!"  # Usando comillas dobles
cadena2 = 'Python es genial.'  # Usando comillas simples
cadena3 = """Esto es una cadena
multilínea."""  # Usando comillas triples

print(cadena1)
print(cadena2)
print(cadena3)


# Operaciones con cadenas

# Concatenación
saludo = cadena1 + " " + cadena2
print("Concatenación:", saludo)

# Repetición
eco = "Hola! " * 3
print("Repetición:", eco)

# Acceso a caracteres
primera_letra = cadena1[0]
ultima_letra = cadena2[-1]
print("Primera letra de cadena1:", primera_letra)
print("Última letra de cadena2:", ultima_letra)

# Subcadenas (slicing)
subcadena = cadena2[0:6]  # Extrae 'Python'
print("Subcadena de cadena2:", subcadena)

# Métodos comunes de cadenas
mayusculas = cadena2.upper()
minusculas = cadena1.lower()
longitud = len(cadena3)
print("Mayúsculas:", mayusculas)
print("Minúsculas:", minusculas)
print("Longitud de cadena3:", longitud)

# Búsqueda y reemplazo
posicion = cadena1.find("Mundo")
reemplazo = cadena2.replace("genial", "increíble")
print("Posición de 'Mundo' en cadena1:", posicion)
print("Reemplazo en cadena2:", reemplazo)

# Formateo de cadenas
nombre = "Ana"
edad = 25
presentacion = "Me llamo {} y tengo {} años.".format(nombre, edad) # Usando el método format() tradicional 
print("Formateo de cadenas:", presentacion)
# Formateo con versiones más recientes de Python 
presentacion_f = f"Me llamo {nombre} y tengo {edad} años."
print("F-strings:", presentacion_f)

# Escape de caracteres
cadena_escape = "Primera línea.\nSegunda línea.\tCon tabulación." # \n es salto de línea, \t es tabulación
print("Escape de caracteres:\n", cadena_escape)
# Cadenas crudas (raw strings)
cadena_cruda = r"C:\nueva_carpeta\archivo.txt" # La r antes de las comillas indica que es una cadena cruda
cadena_normal = "C:\\nueva_carpeta\\archivo.txt" # Equivalente sin usar raw string: cada \\ es una diagonal
print("Cadena cruda:", cadena_cruda)
print("Cadena sin raw string:", cadena_normal)

# Recorrer la cadena, letra por letra. El bucle for se explica en 07_bucles.py
print("Iterar sobre cadena1:")
for char in cadena1:
    print(char, end=' ')
print()

# División de cadenas
partes = cadena1.split(", ")
print("División de cadena1:", partes)

# Unión de cadenas
unida = " - ".join(partes)
print("Unión de partes:", unida)

# Eliminación de espacios en blanco
cadena_espacios = "   Espacios     en     blanco   "
cadena_sin_espacios = cadena_espacios.strip()
print("Cadena sin espacios:", cadena_sin_espacios)

# Cadenas multilínea con formato
multilinea_format = """\
Línea 1: {0}
Línea 2: {1}
Línea 3: {2}\
""".format("Primera", "Segunda", "Tercera")
print("Cadenas multilínea con formato:\n", multilinea_format)

# Convertir otros tipos a cadena
numero = 42
cadena_numero = str(numero)
print("Número convertido a cadena:", cadena_numero)

# Convertir cadena a lista de caracteres
lista_caracteres = list(cadena1)
print("Lista de caracteres de cadena1:", lista_caracteres)

# Convertir lista de caracteres a cadena
cadena_desde_lista = ''.join(lista_caracteres)
print("Cadena desde lista de caracteres:", cadena_desde_lista)

# Métodos adicionales útiles
inicio = cadena1.startswith("Hola") # Verifica si cadena1 empieza con "Hola"
fin = cadena2.endswith("genial.") # Verifica si cadena2 termina con "genial."
print("cadena1 empieza con 'Hola':", inicio)
print("cadena2 termina con 'genial.':", fin)

# Contar ocurrencias de un carácter
contador_o = cadena1.count('o')
print("Número de veces que 'o' aparece en cadena1:", contador_o)


