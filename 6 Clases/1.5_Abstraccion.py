# 1.1 Introduccion
    # No las vamos a instanciar nunca directamente
    # Contienen por lo menos un metodo abstracto
    # Las vamos a usar de bases para otras subclases que heredan de la superclase
    # Sirven para sobreescribir metodos en otras subclases
    # Como minimo una clase abstarcta debe tener un metodo abstracto

from abc import ABC, abstractclassmethod # ABC nos permmite hacer una clase abstracta

class Personaje(ABC):
    # Un decorador envuelve o modifica el comportamiento de un metodo
    # Convertimos el metodo init en abstract
    # Por tanto las tenemos que redifinir en otras subclases
    @abstractclassmethod # Utilizando un decorador de python
    def __init__(self, nombre):
        self.nombre = nombre
        self.nivel = 0
        self.inventario = []
        self.vida = 100

    # Es para que las demas subcalses puedan redifinir este metodo
    @abstractclassmethod
    def atacar(self, objetivo):
        pass # El pass es para asegurar que las subclases puedan redefinir este metodo

    @abstractclassmethod
    def getStatus(self):
        print (f"Nombre: {self.nombre}. Nivel: {self.nivel}")

    def subirNivel(self):
        self.nivel += 1

    def verInventario(self):
        print (f"Inventario de {self.nombre}")
        for objeto in self.inventario:
            print (objeto)


# En la subclas Mago tenemos que sobreescrivir todos los metodos que hemos hecho abstarctos 
class Mago(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 120
        self.inteligencia = 95
        self.inventario = ["Grimorio", "Baston magico"]

    def getStatus(self):
        print ("Clase mago")
        super().getStatus()

    def atacar(self, objetivo):
        objetivo.vida -= self.inteligencia * 0.6
        print (f"Vida actual del objetivo es {objetivo.vida}")
    
    
class Gerrero(Personaje):
    def __init__(self, nombre):
        super().__init__(nombre)
        self.vida = 200
        self.fuerza = 75
        self.inventario = ["Pocion de vida", "Escudo", "Espada"]

    def getStatus(self):
        print ("Clase Guerrero")
        super().getStatus()

    def atacar(self, objetivo):
        objetivo.vida -= self.fuerza * 0.8
        print (f"Vida actual del objetivo es {objetivo.vida}")


guerrero = Gerrero("Liones") 
mago = Mago("Yuno")

guerrero.getStatus()
mago.getStatus()

guerrero.verInventario()
mago.verInventario()

guerrero.atacar(mago)
mago.atacar(guerrero)


