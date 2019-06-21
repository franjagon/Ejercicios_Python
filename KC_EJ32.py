'''
    KC_EJ32
    Crear una clase Modulo con los siguientes atributos: listado_alumnos, fecha_inicio, fecha_fin.
    El listado de alumnos deberá ser tipo Lista y contener objetos de tipo Alumno (KC_EJ31).
    En la misma clase modulo deberá implementar métodos para:
        · Agregar objetos Alumno al listado de alumnos.
        · Buscar un Alumno.
        · Mostrar todos los alumnos con estatus_inscrito True.
'''


import KC_EJ31


class Modulo():
    
    def __init__(self, fecha_inicio, fecha_fin, n):      
        self.listado_alumnos = []
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        
        for i in range(0, n):
            self.agregarAlumno()
        
    def agregarAlumno(self):
        alumno = KC_EJ31.Alumno()
        self.listado_alumnos.append(alumno)
        
    def buscarAlumno(self, matricula):
        encontrado = False
        
        for n in range(0, len(self.listado_alumnos)):
            if self.listado_alumnos[n].numero_matricula == matricula:
                encontrado = True
                print("\n", self.listado_alumnos[n].numero_matricula)
                print("", self.listado_alumnos[n].nombre)
                print("", self.listado_alumnos[n].apellido)
                print("", self.listado_alumnos[n].correo_electronico)
                print("", self.listado_alumnos[n].estatus_inscrito)
            
        if encontrado == False:
            print("\nNo existe ningún alumno con el número de matrícula {}".format(matricula))
        
    def mostrarInscritos(self):
        for n in range(0, len(self.listado_alumnos)):
            if self.listado_alumnos[n].estatus_inscrito == True:
                print("\n", self.listado_alumnos[n].numero_matricula)
                print("", self.listado_alumnos[n].nombre)
                print("", self.listado_alumnos[n].apellido)
                print("", self.listado_alumnos[n].correo_electronico)
                print("", self.listado_alumnos[n].estatus_inscrito)
                
'''  
if __name__ == "__main__":
    Modulo1 = Modulo("2019-06-21", "2020-04-21", 5)
    
    print("\nBuscamos al alumno con matricula 1")
    Modulo1.buscarAlumno(1)
    
    print("\nBuscamos al alumno con matricula 5")
    Modulo1.buscarAlumno(5)
    
    print("\nMostramos los alumnos inscritos (2 y 4)")
    Modulo1.mostrarInscritos()
'''