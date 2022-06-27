
class Alumno:
    
    nombre = "jOel"

    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setNota(self, nota):
        self.nota = nota

    def getNota(self):
        return self.nota

    def aprobarAlumno(self):
        if self.nota > 7:
            print (f"El alumno {self.nombre} aprobo la materia")
        else:
            print (f"El alumno {self.nombre} no aprobo")        
                     
claseA = Alumno()
print (claseA.getNombre())
claseA.setNota(9)
print (claseA.getNota())
claseA.aprobarAlumno()





    

