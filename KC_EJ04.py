'''
    KC_EJ04
    Crea un programa que solicite tres notas y muestre su media.
'''


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_nota(msg):
    nota_pedida = None

    while nota_pedida is None:
        nota_pedida = valida_nota(input(msg))

        if nota_pedida is None:
            print("\n\tNota no válida. Se solicita un valor numérico entre 0 y 10.\n")

    return nota_pedida


# Función que se encarga de validar que el valor que le llega es numérico entre 0 y 10 o devolverá 'None'
def valida_nota(str_nota):
    try:
        nota_valida = float(str_nota)

        if nota_valida < 0 or nota_valida > 10:
            nota_valida = None
    except:
        nota_valida = None

    return nota_valida


# Ejecución del código principal
if __name__ == "__main__":
    lista_notas = []
    suma = 0
    for n in range(0, 3):
        lista_notas.append(pide_nota("Introduce una nota: "))
        suma += lista_notas[n]

    print("\nLa media de las notas introducidas es: {}".format(round(suma/len(lista_notas), 2)))
