# el meotod init se ejecuta por defecto al crear un onbejto de la clase
# el init definen caracterisyicas iniciales a los atributos

class Camiseta:
    def __init__(self, marca, precio, color):  # self es una referecnia al objeto creado de una clase
        # inicializamos los atributos 
        self.marca = marca
        self.precio = precio
        self.color = color

    def aplicarDescuento(self, porcentaje): # Self toma atributos de un unico objeto 
        self.precio = self.precio - self.precio * porcentaje / 100 # con self tomamos los atributos de un obejto

        
camiseta1 = Camiseta("Adidas", 30, "blanca") # Creamo suna instancia de la clase y camiseta1 es un objeto de la clase

print ("precio = " + str(camiseta1.precio))
camiseta1.aplicarDescuento(50)
print ("descuento = " + str(camiseta1.precio))

# 2.- Ingresar valores el el constructor

import math as m

class Calculadora:
    def __init__(self): # Metodo constructor
        self.numero1 = int(input("Ingrese el primer numero: ")) # El usuario inicializa los atributos
        self.numero2 = int(input("Ingrese el segundo numero: "))

    def suma(self):
        print (f"La suma es: {self.numero1 + self.numero2}")

    def resta(self):
        print (f"La resta es: {self.numero1 - self.numero2}")

    def dividir(self):
        print (f"La division es: {self.numero1 / self.numero2}")

    def multiplicacion(self):
        print (f"La multiplicacion es: {self.numero1 * self.numero2}")

    def potencia(self):
        print (f"La potencia es: {m.pow(self.numero1, self.numero2)}")


calcular = Calculadora()
calcular.suma()
calcular.resta()
calcular.dividir()
calcular.multiplicacion()
calcular.potencia()


