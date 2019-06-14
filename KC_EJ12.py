'''
    KC_EJ12
    Crear un programa que reciba una letra e indique si es vocal o consonante.
'''

_ASCII_VOC = (65, 69, 73, 79, 85, 97, 101, 105, 111, 117, 192, 193, 194, 195, 196, 197, 200, 201, 202, 203, 204, 
              205, 206, 207, 210, 211, 212, 213, 214, 216, 217, 218, 219, 220, 224, 225, 226, 227, 228, 229, 232, 
              233, 234, 235, 236, 237, 238, 239, 242, 243, 244, 245, 246, 248, 249, 250, 251, 252)
_ASCII_CON = (66, 67, 68, 70, 71, 72, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 86, 87, 88, 89, 90, 98, 99, 100, 102, 
              103, 104, 106, 107, 108, 109, 110, 112, 113, 114, 115, 116, 118, 119, 120, 121, 122, 199, 209, 221, 
              231, 241, 253, 255, 376)
_VC = {'V': 'vocal', 'C': 'consonante'}


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_letra(msg):
    letra_pedida = None
    vOc = None

    while letra_pedida is None:
        letra_pedida, vOc = valida_letra(input(msg))

        if letra_pedida is None:
            print("\n\tEntrada errónea.\n")

    return letra_pedida, vOc


# Función que se encarga de validar que el valor que le llega es una letra, o devolverá 'None'
def valida_letra(str_letra):
    if ord(str_letra) in _ASCII_VOC:
        vOc = 'V'
    elif ord(str_letra) in _ASCII_CON:
        vOc = 'C'
    else:
        str_letra = None
        vOc = None

    return str_letra, vOc


# Ejecución del código principal
if __name__ == "__main__":
    letra, vOc = pide_letra("Introduce una letra: ")

    print("\nLa letra {} es una {}.".format(letra, _VC[vOc]))


