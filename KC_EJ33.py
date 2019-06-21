'''
    KC_EJ33
    Usando las clases Alumno (KC_EJ31) y Modulo (KC_EJ32), crear un programa que contenga una instancia de la clase Modulo, con instancias de alumnos predefinidos en init.
    El programa permitirá al usuario:
        · Ver todos los alumnos matriculados.
        · Ver todos los alumnos inscritos.
        · Buscar un Alumno por matrícula.
'''


import KC_EJ32


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_opcion(msg):
    opcion_pedida = None

    while opcion_pedida is None:
        opcion_pedida = valida_opcion(input(msg))

        if opcion_pedida is None:
            print("\n\tOpción no válida.\n")

    return opcion_pedida


# Función que se encarga de validar que el valor que le llega es numérico entero entre 0 y 3, o devolverá 'None'
def valida_opcion(str_opcion):
    try:
        opcion_valida = int(str_opcion)

        if opcion_valida < 0 or opcion_valida > 3:
            opcion_valida = None
    except:
        opcion_valida = None

    return opcion_valida


# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido
def pide_matricula(msg):
    matricula_pedida = None

    while matricula_pedida is None:
        matricula_pedida = valida_matricula(input(msg))

        if matricula_pedida is None:
            print("\n\tOpción no válida.\n")

    return matricula_pedida


# Función que se encarga de validar que el valor que le llega es numérico entero entre 0 y 3, o devolverá 'None'
def valida_matricula(str_matricula):
    try:
        matricula_valida = int(str_matricula)

        if matricula_valida < 0:
            matricula_valida = None
    except:
        matricula_valida = None

    return matricula_valida


if __name__ == "__main__":
    Bootcamp_BD_ML = KC_EJ32.Modulo("2019-06-21", "2020-04-21", 5)
    
    fin = False
    
    while not fin:
        opcion = pide_opcion("\nIntroduce una opción:\n\t0 --> Terminar.\n\t1 --> Ver todos los alumnos matriculados.\n\t2 --> Ver todos los alumnos inscritos.\n\t3 --> Buscar un alumno.\n\t")
    
        if opcion == 0:
            break
        elif opcion == 1:
            for n in range(1, len(Bootcamp_BD_ML.listado_alumnos) + 1):
                Bootcamp_BD_ML.buscarAlumno(n)
        elif opcion == 2:
            Bootcamp_BD_ML.mostrarInscritos()
        else:
            Bootcamp_BD_ML.buscarAlumno(pide_matricula("Introduce la matrícula a buscar: "))
            