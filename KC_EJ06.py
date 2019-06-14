'''
    KC_EJ06
    Crea un programa que solicite dos números y muestre los resultados de aplicar comparaciones relacionales.
'''


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_numero(msg):
    numero_pedido = None

    while numero_pedido is None:
        numero_pedido = valida_numero(input(msg))

        if numero_pedido is None:
            print("\n\tValor erróneo.\n")

    return numero_pedido


# Función que se encarga de validar que el valor que le llega es numérico, o devolverá 'None'
def valida_numero(str_numero):
    try:
        numero_valido = float(str_numero)
    except:
        numero_valido = None

    return numero_valido


# Ejecución del código principal
if __name__ == "__main__":
    numero_1 = pide_numero("Introduce el primer número: ")
    numero_2 = pide_numero("Introduce el segundo número: ")

    print("\n{} < {} ==> {}".format(numero_1, numero_2, numero_1 < numero_2))
    print("{} > {} ==> {}".format(numero_1, numero_2, numero_1 > numero_2))
    print("{} y {} son iguales ==> {}".format(numero_1, numero_2, numero_1 == numero_2))
    print("{} y {} son distintos ==> {}".format(numero_1, numero_2, numero_1 != numero_2))