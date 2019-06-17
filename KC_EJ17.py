'''
    KC_EJ17
    Crea un programa que contenga un diccionario con nombres y correos electrónicos.
    Solicitar el nombre de una persona y mostrar su correo electrónico.
    Indicar con un mensaje apropiado cuando no se encuentre un resultado válido.
'''

_DICC_EMAIL = {"Pedro": "pedro.picapiedra@gmail.com", "Pablo": "pmarmol123@gmail.com", "Bob": "bob@gmail.com"}


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_nombre(msg):
    nombre = None

    while nombre is None:
        nombre = input(msg)

        if len(nombre) != 0 and nombre.isalnum():
            if nombre not in _DICC_EMAIL.keys():
                nombre = 1
                print("No disponemos del email de esa persona.")

            return nombre
        else:
            nombre = None
            print("Nombre no válido.")


# Ejecución del código principal
if __name__ == "__main__":
    nombre = pide_nombre("Introduce el nombre del dueño del email que deseas ver: ")

    if nombre != 1:
        print("\n{} ==> {}".format(nombre, _DICC_EMAIL[nombre]))
