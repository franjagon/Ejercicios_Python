'''
    KC_EJ26
    Crear un programa con una función pintar_fila() que arme las filas de una tabla HTML.
    Completar el programa con la estructura de una tabla e invocando a la función N veces, donde N es un valor introducido por el usuario.
'''


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_numero(msg):
    numero_pedido = None

    while numero_pedido is None:
        numero_pedido = valida_numero(input(msg))

        if numero_pedido is None:
            print("\n\tNúmero no válido. Pon un valor numérico entero.\n")

    return numero_pedido


# Función que se encarga de validor que el valor que le llega es numérico y mayor que uno, o devolverá 'None'
def valida_numero(str_numero):
    try:
        numero_valido = int(str_numero)

        if numero_valido < 1:
            numero_valido = None
    except:
        numero_valido = None

    return numero_valido


# Función que se encarga de pintar una fila de una tabla HTML
def pintar_fila():
    print("\t\t<tr><td></td></tr>")


# Ejecución del código principal
if __name__ == "__main__":
    numero = pide_numero("Introduce un número de filas para la tabla HTML: ")
    print("\t<table>\n\t\t#Ciclo invocando {} veces a la función pintar_fila()".format(numero))
    
    for n in range(0, numero):
        pintar_fila()
    
    print("\t\t#- - - fin ciclo\n\t</table>")