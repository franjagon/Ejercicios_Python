'''
    KC_EJ03
    Crea un programa que solicite una cantidad en Euros y muestre su equivalente en USD.
    Fijamos la equivalencia: 1€ = 1.13$
'''


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_cantidad(msg):
    cantidad_pedida = None

    while cantidad_pedida is None:
        cantidad_pedida = valida_cantidad(input(msg))

        if cantidad_pedida is None:
            print("\n\tCantidad no válida.\n")

    return cantidad_pedida


# Función que se encarga de validar que el valor que le llega es numérico natural o devolverá 'None'
def valida_cantidad(str_cantidad):
    try:
        cantidad_valida = float(str_cantidad)

        if cantidad_valida < 0:
            cantidad_valida = None
    except:
        cantidad_valida = None

    return cantidad_valida


# Ejecución del código principal
if __name__ == "__main__":
    cantidad = pide_cantidad("Introduce una cantidad en euros: ")

    print("\n{}€ son {}$".format(cantidad, round(cantidad * 1.13, 2)))
