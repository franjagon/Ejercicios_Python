'''
    KC_EJ24
    Modificar el programa KC_EJ23 para que muestre los resultados ordenados por la media de forma descendente.
'''
    
_FIN = "terminar"

    
# Función que se encarga de solicitar el dato al usuario mientras no introduzca un valor válido. La primera vez no permite "terminar". 
def pide_nombre(msg, i):
    nombre = None

    while nombre is None:
        nombre = input(msg)

        if nombre == _FIN and i == 0:
            nombre = None
            print("\n\tNombre no válido.\n")
        else:
            if len(nombre) != 0 and len(nombre) > 2 and nombre.isalnum():
                return nombre
            else:
                nombre = None
                print("\n\tNombre no válido.\n")

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
    lista_medias = []
    
    fin = False
    i = 0

    while not fin:
            
        dic_alumno = {"Nombre": "", "Matemáticas": 0.0, "Física": 0.0, "Química": 0.0}

        for key in dic_alumno.keys():
            if key == "Nombre":
                
                if i > 0:
                    print("\nPara dejar de introducir alumnos, escribe: 'terminar'.")
                    
                dic_alumno[key] = pide_nombre("Introduce el nombre del alumno: ", i)
                
                if dic_alumno["Nombre"] == _FIN:
                    print("")
                    break
            else:
                dic_alumno[key] = pide_nota("Introduce su nota de {}: ".format(key))
        
        if dic_alumno["Nombre"] != _FIN:
            lista_alumnos.append(dic_alumno)
        else:
            fin = True
            
        i += 1

    for n in range(0, len(lista_alumnos)):
        suma = 0
        par = []
        nombre = ""
        
        for key in lista_alumnos[n].keys():
            if key == "Nombre":
                nombre = lista_alumnos[n][key]
            else:
                suma += lista_alumnos[n][key]
        
        par.append(round(suma / 3, 2))
        par.append(nombre)
        lista_medias.append(par)
        
    lista_medias.sort(reverse = True)
    
    for n in range(0, len(lista_medias)):
        print("{}:\t\t{}".format(lista_medias[n][1], lista_medias[n][0]))

