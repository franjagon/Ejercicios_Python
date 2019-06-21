'''
    KC_EJ28
    Crear un programa que contenga una función pintar_rectangulo(lado, figura).
    Esta función debera pintar en consola un cuadrilátero de lado x lado con la figura proporcionada.
'''

    
# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_lado(msg):
    lado_pedido = None

    while lado_pedido is None:
        lado_pedido = valida_lado(input(msg))

        if lado_pedido is None:
            print("\n\tNúmero no válido. Se solicita un valor numérico entero.\n")

    return lado_pedido


# Función que se encarga de validor que el valor que le llega es numérico y mayor que uno, o devolverá 'None'
def valida_lado(str_lado):
    try:
        lado_valido = int(str_lado)

        if lado_valido < 1:
            lado_valido = None
    except:
        lado_valido = None

    return lado_valido


# Función que se encarga de solicitar el figura al usuario mientras no introduzca un valor válido
def pide_figura(msg):
    figura = None

    while figura is None:
        figura = input(msg)

        if len(figura) == 1:
            return figura
        else:
            figura = None
            print("\n\tFigura no válida.\n")

  
# Función que se encarga de pintar el rectangulo
def pintar_rectangulo(lado, figura):
    for n in range (0, lado):
        for m in range(0, lado):
            if n == 0 or n == lado - 1:
                print(figura, end = "")
            elif m == 0 or m == lado - 1:
                print(figura, end = "")
            else:
                print(" ", end = "")
        print("")


# Ejecución del código principal
if __name__ == "__main__":

    lado = pide_lado("Introduce un valor para el lado del cuadrilátero: ")
    figura = pide_figura("Introduce una figura para pintar el cuadrilátero: ")
    
    pintar_rectangulo(lado, figura)

