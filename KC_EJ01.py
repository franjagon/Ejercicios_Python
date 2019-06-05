'''
    KC_EJ01
    Crea un programa por el cual se solicite al usuario el radio de un círculo.
    El programa deberá calcular y mostrar el área.
'''


# Importamos la librería 'math' para poder hacer uso de la constante 'pi'
from math import *


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_radio(msg):
    radio_pedido = None

    while radio_pedido is None:
        radio_pedido = valida_radio(input(msg))

        if radio_pedido is None:
            print("\n\tEse valor no puede ser la medida del radio de un círculo.\n")

    return radio_pedido


# Función que se encarga de validar que el valor que le llega es numérico positivo o devolverá 'None'
def valida_radio(str_radio):
    try:
        radio_valido = float(str_radio)

        if radio_valido <= 0:
            radio_valido = None
    except:
        radio_valido = None

    return radio_valido


# Ejecución del código principal
if __name__ == "__main__":
    radio = pide_radio("Introduce la medida del radio de un circulo: ")

    print("\nEl area de un círculo con radio {} es {}".format(radio, round(pi * (radio ** 2), 2)))
