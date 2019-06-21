'''
    KC_EJ22
    Crea un programa que reciba los nombres y edades de tres personas.
    Mostrar únicamente los nombres de las personas que tienen derecho a votar (mayores de 18 años).
'''

# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_nombre(msg):
    nombre = None

    while nombre is None:
        nombre = input(msg)

        if len(nombre) != 0 and len(nombre) > 2 and nombre.isalnum():
            return nombre
        else:
            nombre = None
            print("Nombre no válido.")


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_edad(msg):
    edad_pedida = None

    while edad_pedida is None:
        edad_pedida = valida_edad(input(msg))

        if edad_pedida is None:
            print("\n\tEdad no válida.")

    return edad_pedida


# Función que se encarga de validar que el valor que le llega es numérico entero y mayor que 0, o devolverá 'None'
def valida_edad(str_edad):
    try:
        edad_valida = int(str_edad)

        if edad_valida < 1:
            edad_valida = None
    except:
        edad_valida = None

    return edad_valida


# Ejecución del código principal
if __name__ == "__main__":
    votantes = []

    for n in range(0, 10):
        nombre = pide_nombre("Introduce el nombre de la Persona número {}: ".format(n + 1))
        edad = pide_edad("Introduce su edad: ")

        if edad > 17:
            votantes.append(nombre)
    
    if len(votantes) == 0:
        print("\nNinguna de estas VOTANTES tiene aun derecho a votar.")
    else:
        print("\nTienen derecho a votar: ", end = "")
        
        for n in range (0, len(votantes)):
            separador = ", "
            
            if n == len(votantes) - 2:
                separador = " y "
            elif n == len(votantes) - 1:
                separador = "."

            print("{}{}".format(votantes[n], separador), end = "")
            