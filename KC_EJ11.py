'''
    KC_EJ11
    Crear un programa que reciba tres números e indique cuál es el mayor y el menor.
'''


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_numero(msg):
    numero_pedido = None

    while numero_pedido is None:
        numero_pedido = valida_numero(input(msg))

        if numero_pedido is None:
            print("\n\tEntrada no válida.\n")

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
    lista_numeros = []

    for n in range(0, 3):
        lista_numeros.append(pide_numero("Introduce un número: "))

    print("\nEl número menor es: {}.\nEl número mayor es: {}.".format(min(lista_numeros), max(lista_numeros)))
