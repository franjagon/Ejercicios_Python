'''
    KC_EJ34
    Crear las clase AlumnoRemoto y AlumnoPresencial, ambas subclases de la clase Alumno (KC_EJ3R).
        · AlumnoRemoto debera contar con los atributos: numero_matricula, nombre, apellido, correo_electronico, estatus_inscrito, skype, huso_horario.
        · AlumnoPresencial debera contar con los atributos: numero_matricula, nombre, apellido, correo_electronico, estatus_inscrito, numero_asiento.
'''


import KC_EJ31


class AlumnoRemoto(KC_EJ31.Alumno):
    
    def __init__(self):
        KC_EJ31.Alumno.__init__(self)
        self.skype = self.__pideAtributoRemoto("S")
        self.huso_horario = self.__pideAtributoRemoto("H")
        

    # Función que se encarga de validar que el valor que le llega es un texto (y en su caso, un correo electrónico), o devolverá 'None'
    def __valAtributoRemoto(self, str_txt, txt):
        
        if (txt == "H" and str_txt.upper().find("UTC") == -1 and (str_txt.find("+") == -1 or str_txt.find("-") == -1)):
            str_txt = None
        elif str_txt.isdigit():
            str_txt = None

        return str_txt
    

    # Función para introducir el nombre o el apellido del alumno    
    def __pideAtributoRemoto(self, txt):
        SH = None
            
        if txt == "S":
            valor = "skype"            
        if txt == "H":
            valor = "huso horario"
            
        while SH == None:
            SH = self.__valAtributoRemoto(input("\nIntroduce el {} del alumno: ".format(valor)), txt)
            
            if SH == None:
                print("\nEntrada no válida. Debes introducir un {} correcto".format(valor))
                
        return SH


class AlumnoPresencial(KC_EJ31.Alumno):
    
    def __init__(self):
        KC_EJ31.Alumno.__init__(self)
        self.numero_asiento = self.__pideAtributoPresencial()
        

    # Función que se encarga de validar que el valor que le llega es un texto (y en su caso, un correo electrónico), o devolverá 'None'
    def __valAtributoPresencial(self, str_txt):        
        try:
            str_txt = int(str_txt)

            if str_txt < 0:
                str_txt = None            
        except:
            str_txt = None

        return str_txt
    

    # Función para introducir el nombre o el apellido del alumno    
    def __pideAtributoPresencial(self):
        P = None

        valor = "numero de asiento"
            
        while P == None:
            P = self.__valAtributoPresencial(input("\nIntroduce el {} del alumno: ".format(valor)))
            
            if P == None:
                print("\nEntrada no válida. Debes introducir un {} correcto".format(valor))
                
        return P
    
'''   
if __name__ == "__main__":
    AlumnoR = AlumnoRemoto()
    AlumnoP = AlumnoPresencial()
    
    print("\n", AlumnoR.numero_matricula)
    print("", AlumnoR.nombre)
    print("", AlumnoR.apellido)
    print("", AlumnoR.correo_electronico)
    print("", AlumnoR.estatus_inscrito)
    print("", AlumnoR.skype)
    print("", AlumnoR.huso_horario)
    
    print("\n", AlumnoP.numero_matricula)
    print("", AlumnoP.nombre)
    print("", AlumnoP.apellido)
    print("", AlumnoP.correo_electronico)
    print("", AlumnoP.estatus_inscrito)
    print("", AlumnoP.numero_asiento)
'''    