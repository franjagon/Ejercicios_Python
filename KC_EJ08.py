'''
    KC_EJ08
    Crea un programa que reciba un número entero y muestre si es par o impar, positivo o negativo, o cero.
'''


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_numero(msg):
    numero_pedido = None

    while numero_pedido is None:
        numero_pedido = valida_numero(input(msg))

        if numero_pedido is None:
            print("\n\tValor erróneo.\n")

    return numero_pedido


# Función que se encarga de validar que el valor que le llega es numérico entero, o devolverá 'None'
def valida_numero(str_numero):
    try:
        numero_valido = int(str_numero)
    except:
        numero_valido = None

    return numero_valido


# Ejecución del código principal
if __name__ == "__main__":
    numero = pide_numero("Introduce un número: ")

    if numero % 2 == 0:
        r1 = "par"
    else:
        r1 = "impar"

    if numero > 0:
        r2 = "positivo"
    elif numero < 0:
        r2 = "negativo"

    if numero == 0:
        print("\nEl número introducido es cero.")
    else:
        print("\nEl número {} es {} y {}.".format(numero, r1, r2))