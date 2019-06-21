'''
    KC_EJ31
    Crear una clase Alumno con los siguientes atributos: numero_matricula, nombre, apellido, correo_electronico, estatus_inscrito.
    La matrícula deberá ser numérica, mientras que el coreo electrónico, el nombre y el apellido deberan ser textos. El estátus deberá ser un booleano.
'''


class Alumno():
    
    def __init__(self):      
        self.numero_matricula = self.__pideAtributo("M")
        self.nombre = self.__pideAtributo("N")
        self.apellido = self.__pideAtributo("A")
        self.correo_electronico = self.__pideAtributo("C")
        self.estatus_inscrito = self.__pideAtributo("E")
        

    # Función que se encarga de validar que el valor que le llega es un texto (y en su caso, un correo electrónico), o devolverá 'None'
    def __valAtributo(self, str_txt, txt):
        _SN = ("S", "N")
        posibleDoble = []
        
        if txt == "M":            
            try:
                str_txt = int(str_txt)

                if str_txt < 0:
                    str_txt = None            
            except:
                str_txt = None
        else:        
            if (txt == "C" and str_txt.find("@") == -1) or (txt == "E" and str_txt.upper() not in _SN):
                str_txt = None
            else:
                if txt == "N" or txt == "A":
                    posibleDoble = str_txt.split(" ")
                elif txt == "C":
                    posibleDoble = str_txt.split("@")
                elif txt == "E":
                    posibleDoble.append(str_txt)
                    
                for n in range(0, len(posibleDoble)):
                    if posibleDoble[n].isdigit():
                        str_txt = None
                    elif txt == "E" and posibleDoble[n].upper() == "S":
                        str_txt = True
                    elif txt == "E" and posibleDoble[n].upper() == "N":
                        str_txt = False

        return str_txt
    

    # Función para introducir el nombre o el apellido del alumno    
    def __pideAtributo(self, txt):
        MNACE = None
            
        if txt == "M":
            valor = "número de matrícula"            
        if txt == "N":
            valor = "nombre"
        elif txt == "A":
            valor = "apellido"
        elif txt == "C":
            valor = "correo electrónico"
        elif txt == "E":
            valor = "estatus de inscrito (S/N)"
            
        while MNACE == None:
            MNACE = self.__valAtributo(input("\nIntroduce el {} del alumno: ".format(valor)), txt)
            
            if MNACE == None:
                print("\nEntrada no válida. Debes introducir un {} correcto".format(valor))
                
        return MNACE
    
'''    
if __name__ == "__main__":
    Alumno1 = Alumno()
    Alumno2 = Alumno()
    print("\n", Alumno1.numero_matricula)
    print("", Alumno1.nombre)
    print("", Alumno1.apellido)
    print("", Alumno1.correo_electronico)
    print("", Alumno1.estatus_inscrito)
    
    print("\n", Alumno2.numero_matricula)
    print("", Alumno2.nombre)
    print("", Alumno2.apellido)
    print("", Alumno2.correo_electronico)
    print("", Alumno2.estatus_inscrito)
'''
    
