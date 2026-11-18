# Tema 4.5 Closures
# Una función interna puede recordar variables de donde fue creada,
# aunque la función de afuera ya haya terminado.
# Así se arma una función que ya trae un dato guardado.

def crear_multiplicador(factor):
    def multiplicar(numero):
        return numero * factor  # factor sigue disponible aquí
    return multiplicar

por_tres = crear_multiplicador(3)
# crear_multiplicador ya terminó, y por_tres sigue recordando el 3
print("por_tres(10):", por_tres(10))
print("por_tres(4):", por_tres(4))

por_diez = crear_multiplicador(10)
print("por_diez(10):", por_diez(10))  # este recuerda el 10, no el 3

# En la vida real sirve para fijar un dato una sola vez.
# El IVA general en México es 16 % y en la frontera es 8 %.
# Cada función se queda con su tasa.
def crear_iva(tasa):
    def calcular(monto):
        impuesto = monto * tasa
        total = monto + impuesto
        return impuesto, total
    return calcular

iva_general = crear_iva(0.16)
iva_frontera = crear_iva(0.08)

impuesto, total = iva_general(1000)
print("IVA 16%:", impuesto, "Total:", total)

impuesto, total = iva_frontera(1000)
print("IVA 8%:", impuesto, "Total:", total)
