'''
    KC_EJ10
    Crea un programa que reciba un número del 1 a 9 y muestre el nombre de la pelicula Star Wars correspondiente.
    Valdrán los números romanos.
'''

_NUM = ("1", "2", "3", "4", "5", "6", "7", "8", "9")
_ROM = ("I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")
_SWT = ("I - La Amenaza Fantasma",
        "II - El Ataque de los Clones",
        "III - La Venganza de los Sith",
        "IV - Una Nueva Esperanza",
        "V - El Imperio Contraataca",
        "VI - El Retorno del Jedi",
        "VII - El Despertar de la Fuerza",
        "VIII - Los Últimos Jedi",
        "IX - El Ascenso de Skywalker")


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_opcion(msg):
    opcion_pedida = None

    while opcion_pedida is None:
        opcion_pedida = valida_opcion(input(msg))

        if opcion_pedida is None:
            print("\n\tEntrada errónea.\n")

    return opcion_pedida


# Función que se encarga de validar que el valor que le llega es un número del 1 al 9, o devolverá 'None'
def valida_opcion(str_opcion):
    if str_opcion in _NUM:
        indice = _NUM.index(str_opcion)
    elif str_opcion.upper() in _ROM:
        indice = _ROM.index(str_opcion.upper())
    else:
        indice = None

    return indice


# Ejecución del código principal
if __name__ == "__main__":
    opcion = pide_opcion("Introduce uno de los 9 primeros números (puedes hacerlo en notación romana): ")

    print("\nStar Wars {}.".format(_SWT[opcion]))