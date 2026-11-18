# Mini curso de Python

Este curso recorre los elementos básicos de Python y, cuando ya hay con qué sostenerlos, entra en temas de nivel intermedio. Cada archivo es un ejemplo que se puede ejecutar solo. Los comentarios van junto al código y explican la idea con calma.

Sirve para quien está empezando y también para quien ya escribe programas pequeños y quiere entender cómo una función puede transformar datos, filtrarlos o recordar un valor.

## Qué se ve

Conviene seguir el número de los archivos. Lo que aparece después se apoya en lo anterior.

### Elementos básicos

| Archivo | Tema |
| --- | --- |
| `01_variables.py` | Variables, tipos de dato y cómo nombrarlas |
| `02_operadores.py` | Cuentas, comparaciones y operaciones lógicas |
| `03_cadenas.py` | Texto: unir, cortar, buscar y dar formato |
| `04_listas.py` | Listas para guardar varios valores y modificarlos |
| `05_tuplas.py` | Tuplas, que conservan sus valores después de crearse |
| `06_condicionales.py` | Decisiones con `if`, `elif` y `else` |
| `07_bucles.py` | Repetición con `for` y `while` |
| `08_funciones.py` | Funciones con nombre, parámetros y valor de regreso |

Con esto ya se puede guardar un dato, decidir qué hacer con él, recorrerlo y encerrar un cálculo en una función.

### Un paso más allá

Desde el archivo 09 la función también es un valor del programa: se puede guardar en una variable, pasar a otra función y devolver. Estos temas ya son de nivel intermedio.

| Archivo | Tema |
| --- | --- |
| `09_caracteristicas_funcionales.py` | Guardar funciones, calcular sin modificar los datos originales |
| `10_funciones_orden_superior.py` | Funciones que reciben otra función, o que devuelven una |
| `11_funciones_anonimas.py` | `lambda`, para funciones de una sola expresión |
| `12_map_filter_reduce.py` | Transformar, filtrar y resumir una lista |
| `13_closures.py` | Funciones que recuerdan un dato, como una tasa de IVA |

## Por qué vale la pena entenderlo

Estos conceptos aparecen en cuanto el programa deja de ser un ejemplo corto.

Una función con nombre evita copiar el mismo cálculo en varias partes. Si el cálculo cambia, se corrige en un solo lugar.

Pasar una función como argumento permite reutilizar un recorrido. La misma estructura puede sumar, duplicar o filtrar: cambia la función, no todo el código.

`map`, `filter` y `reduce` ponen nombre a tres tareas muy comunes. `map` transforma cada elemento. `filter` se queda con los que cumplen una condición. `reduce` resume la lista en un solo valor, por ejemplo una suma.

Un closure deja un dato guardado dentro de la función. Así se puede fijar una tasa de IVA o un descuento una sola vez y usar ese cálculo con muchos montos, sin volver a pasar el porcentaje en cada llamada.

## Ejercicios

Los archivos `Ejercicio_01.py` a `Ejercicio_06.py` traen el enunciado y los datos de inicio. La solución se escribe en el mismo archivo.

| Ejercicio | Qué practica |
| --- | --- |
| `Ejercicio_01.py` | `map` para pasar nombres a mayúsculas |
| `Ejercicio_02.py` | `filter` con dos condiciones a la vez |
| `Ejercicio_03.py` | Encadenar `filter`, `map` y `reduce` |
| `Ejercicio_04.py` | Escribir una función que reciba otra función |
| `Ejercicio_05.py` | Reescribir una función corta como `lambda` |
| `Ejercicio_06.py` | Armar un closure que recuerde un saludo |

