'''
    KC_EJ19
    Crea un programa que almacene 10 números dados por el usuario y muestre únicamente los pares.
'''


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_numero(msg):
    numero_pedido = None

    while numero_pedido is None:
        numero_pedido = valida_numero(input(msg))

        if numero_pedido is None:
            print("\n\tValor erróneo.\n")

    return numero_pedido


# Función que se encarga de validar que el valor que le llega es entero, o devolverá 'None'
def valida_numero(str_numero):
    try:
        numero_valido = int(str_numero)
    except:
        numero_valido = None

    return numero_valido


# Ejecución del código principal
if __name__ == "__main__":

    lista = []
    pares = []

    for n in range(0, 10):
        numero = pide_numero("Introduce un número entero ({} de 10): ".format(n + 1))

        lista.append(numero)

        if numero % 2 == 0:
            pares. append(numero)

    print("\nLa lista es: {}".format(lista))
    print("\nLos pares son: {}".format(pares))
