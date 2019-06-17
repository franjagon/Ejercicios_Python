'''
    KC_EJ21
    Crea un programa que reciba un numero natural y muestre su tabla de multiplicar del 1 al 10.
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

    for n in range(1, 11):
        print("{} x {} = {}".format(numero, n, numero * n))
