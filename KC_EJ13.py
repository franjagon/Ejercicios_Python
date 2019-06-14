'''
    KC_EJ13
    Crear un programa que contenga una lista de 20 números y muestre un rango de la lista.
    El inicio y el fin del rango serán introducidos por el usuario y el programa debera validarlos.
'''

_LISTA = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20)


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_numero(msg):
    numero_pedido = None

    while numero_pedido is None:
        numero_pedido = valida_numero(input(msg))

        if numero_pedido is None:
            print("\n\tEntrada no válida.\n")

    return numero_pedido


# Función que se encarga de validar que el valor que le llega es numérico entero positivo, o devolverá 'None'
def valida_numero(str_numero):
    try:
        numero_valido = int(str_numero)

        if numero_valido < 0:
            numero_valido = None

    except:
        numero_valido = None

    return numero_valido


# Ejecución del código principal
if __name__ == "__main__":
    lista_rango = []

    lista_rango.append(pide_numero("Introduce el inicio del rango de la lista que deseas visualizar: "))
    lista_rango.append(pide_numero("Introduce el final del rango de la lista que deseas visualizar: "))

    if lista_rango[0] >= lista_rango[1]:
        print("\nEl inicio del rango no debe ser mayor ni igual al final.")
    elif lista_rango[0] > 19 or lista_rango[1] > 20:
        print("\n Selección fuera del rango (de 0 a 20).")
    else:
        print("\nEl rango solicitado es: {}.".format(_LISTA[lista_rango[0]:lista_rango[1]]))

