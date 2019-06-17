'''
    KC_EJ16
    Crea un programa que contenga una lista de nombres.
    Solicitar un índice de la lista y mostrar el valor del índice.
    El programa deberá validar que el índice es válido.
'''

_TUPLA = ("Pedro Picapiedra", "Pablo Mármol", "Bob Esponja", "Patricio", "Calamardo")

# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_indice(msg):
    indice_pedido = None

    while indice_pedido is None:
        indice_pedido = valida_indice(input(msg))

        if indice_pedido is None:
            print("\n\tValor erróneo.\n")

    return indice_pedido


# Función que se encarga de validar que el valor que le llega es entero y válido para la tupla, o devolverá 'None'
def valida_indice(str_indice):
    try:
        indice_valido = int(str_indice)

        if indice_valido >= len(_TUPLA):
            indice_valido = None

    except:
        indice_valido = None

    return indice_valido


# Ejecución del código principal
if __name__ == "__main__":
    indice = pide_indice("Introduce el índice del valor que deseas ver: ")

    print("\n{} ==> {}".format(indice, _TUPLA[indice]))
