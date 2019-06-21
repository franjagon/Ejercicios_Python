'''
    KC_EJ15
    Crea un programa que reciba el nombre y las calificaciones de tres personas.
    Para cada persona deberá guardar la información en una lista.
    El programa no mostrará resultados de salida.
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
            print("Nombre o apellido no válido.")


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_nota(msg):
    nota_pedida = None

    while nota_pedida is None:
        nota_pedida = valida_nota(input(msg))

        if nota_pedida is None:
            print("\n\tNota no válida. Se solicita un valor numérico entre 0 y 10.\n")

    return nota_pedida


# Función que se encarga de validar que el valor que le llega es numérico entre 0 y 10, o devolverá 'None'
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
    lista_alumnos = []

    for n in range(0, 3):
        dic_Alumno = {"Nombre": "", "Apellido": "",
                      "Matemáticas": 0.0, "Física": 0.0, "Literatura": 0.0, "Gimnasia": 0.0}

        for key in dic_Alumno.keys():
            if key == "Nombre" or key == "Apellido":
                dic_Alumno[key] = pide_nombre("Introduce el {} del alumno número {}: ".format(key, n + 1))
            else:
                dic_Alumno[key] = pide_nota("Introduce su nota de {}: ".format(key))

        lista_alumnos.append(dic_Alumno)

    print(lista_alumnos)
