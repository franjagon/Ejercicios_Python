'''
    KC_EJ18
    Crea un programa que muestre los números naturales del 1 al N, donde N será dado por el usuario.
'''


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_numero(msg):
    numero_pedido = None

    while numero_pedido is None:
        numero_pedido = valida_numero(input(msg))

        if numero_pedido is None:
            print("\n\tValor erróneo.\n")

    return numero_pedido


# Función que se encarga de validar que el valor que le llega es natural, o devolverá 'None'
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
    numero = pide_numero("Introduce un número natural: ")

    lista = []

    for n in range(1, numero + 1):
        lista.append(n)

    print("\n{}".format(lista))
