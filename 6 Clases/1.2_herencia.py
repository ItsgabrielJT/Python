"""Clase que recibe los atributos, metodos y caracteristicas de otra clase"""

#Super clase
class Persona:
    def __init__(self, nombre, edad, Ci):
        self.nombre = nombre
        self.edad = edad
        self.Ci = Ci

    def presentarse(self):
        print (f"Hola !! me llamo {self.nombre} y tengo {self.edad}")

oscar = Persona("OScar", 23, "123343453G")
oscar.presentarse()
print (oscar.Ci + "\n\n-------------------")

#Clase hija
class Trabajador(Persona): # Recibe todas las caracteristicas de la superclase
    def __init__(self, nombre, edad, Ci, sueldo, cargo):
        super().__init__(nombre, edad, Ci) #super() hce referencia a la superclase, por ell pasamos los parametros de persona
        self.sueldo = sueldo
        self.cargo = cargo

    def presentarTrabajador(self):
        print (f"Tengo sueldoo de {self.sueldo} y trabajo en {self.cargo}")

trabajador = Trabajador("Leo", 24, "23131424243H", 123.45, "ingeniero")
trabajador.presentarse()
trabajador.presentarTrabajador()
print (trabajador.Ci + "\n\n-------------------")

#Clase jerarquica
class Estudiante(Persona): # Otra clase hioja que hereda de la misma suoerclase
    def __init__(self, nombre, edad, Ci, curso, universidad):
        super().__init__(nombre, edad, Ci)
        self.curso = curso
        self.universidad = universidad

    def presentarEstudiante(self):
        print (f"Soy de {self.curso} y estudio en {self.universidad}")


estudiante = Estudiante("Leo", 24, "23131424243H", "3A", "EPN")
estudiante.presentarse()
estudiante.presentarEstudiante()
print (estudiante.Ci + "\n\n-------------------")