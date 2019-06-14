'''
    KC_EJ09
    Crea un programa que solicite una cantidad y pregunte si se desea convertirla de Euros a USD o de USD a Euros.
    A la salida debe mostrar el resultado de la conversion.
    Fijamos la equivalencia: 1€ = 1.13$ ; 1$ = 0.89€
'''


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_cantidad(msg):
    cantidad_pedida = None

    while cantidad_pedida is None:
        cantidad_pedida = valida_cantidad(input(msg))

        if cantidad_pedida is None:
            print("\n\tCantidad no válida.\n")

    return cantidad_pedida


# Función que se encarga de validar que el valor que le llega es numérico natural, o devolverá 'None'
def valida_cantidad(str_cantidad):
    try:
        cantidad_valida = float(str_cantidad)

        if cantidad_valida < 0:
            cantidad_valida = None
    except:
        cantidad_valida = None

    return cantidad_valida


# Función que se encarga de solicitar que conversión desea realizar el usuario mientras no introduzca un valor válido
def pide_opcion(msg):
    opcion = None

    while opcion is None:
        opcion = valida_opcion(input(msg))

        if opcion is None:
            print("\n\tOpción no válida.\n")

    return int(opcion)

# Función que se encarga de validar que el valor de opcion elegido es 1 o 2, o devolverá 'None'
def valida_opcion(str_opcion):
    if str_opcion != "0" and str_opcion != "1":
        str_opcion = None
    
    return str_opcion


# Ejecución del código principal
if __name__ == "__main__":
    _CONV = (1.13, 0.89)
    _SYMB = (("€", "$"), ("$", "€"))
    cantidad = pide_cantidad("Introduce una cantidad: ")

    opcion = pide_opcion("¿Qué convertimos?\nPulsa 0 para convertir € en $.\nPulsa 1 para convertir $ en €. ")

    print("\n{}{} son {}{}$".format(cantidad, _SYMB[opcion][0], round(cantidad * _CONV[opcion], 2), _SYMB[opcion][1]))
