# Un metodo o una subclase puede tomar cualquier forma que se le quiera dar

class Empleado:
    def __init__(self, nombre, sueldoMensual):
        self.nombre = nombre
        self.sueldoMensual = sueldoMensual

    def calcularSueldoAnual(self):
        sueldo = 12 * self.sueldoMensual * (1 + 1/100)
        print (f"El sueldo anual de {self.nombre}, es de: $ {sueldo}")


class Contable(Empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)

    def calcularSueldoAnual(self):
        sueldo = 12 * self.sueldoMensual * (1 + 4/100)
        print (f"El sueldo anual de {self.nombre}, Conatble, es de: $ {sueldo}")


class Publicista(Empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)

    def calcularSueldoAnual(self):
        sueldo = 12 * self.sueldoMensual * (1 + 5/100)
        print (f"El sueldo anual de {self.nombre}, Publicista es de: $ {sueldo}")


class Becario(Empleado):
    def __init__(self, nombre, sueldoMensual):
        super().__init__(nombre, sueldoMensual)

    def calcularSueldoAnual(self):
        sueldo = 12 * self.sueldoMensual
        print (f"El sueldo anual de {self.nombre}, Becario es de: $ {sueldo}")

empleados = [
    Empleado("Juan", 100),
    Contable("Hector", 1200),
    Publicista("Rayan", 1300),
    Becario("Pepito", 600)
]

for empresa in empleados:
    empresa.calcularSueldoAnual()