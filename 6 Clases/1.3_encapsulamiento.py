
""" 
    - Permite regular el acceso a metodos o a atributos de la clase
    - El encapsulamiento en python no existe por tanto no existe este funcionamiento
    - Solo esxiste sintaxis hecha por PROGRAMADORES
    """

""" 
    - PROTEGIDO : significa qie puede usarse en clases hijos aparte de las superclases
    - PRIVADO : que solo puede usarse en esa clase
    - PUBLICA : puede usarse en todo el programa(por defecto definido en Python y no se puede cambiar)
    """

"""
    ----------------------------------- CONVENCIONES -------------------------------------
    _atrubuto = un guion bajo al principio de un atributo indica que es protegido
    __atributo = un doble guion bajo al principio significa que es privado
    *** La misma sintaxis aplica para los metodos ***
    - La convencion solo se usa entre programadores para inidcar el uso de metodos y atributos
    """

class Circulo:
    def __init__(self, radio):
        self.__radio = radio
        self.__PI = 3.1415

    def calcularPerimetro(self):
        return 2 * self.__PI * self.__radio

    def calcularArea(self):
        return self.__PI * self.__radio ** 2

    def getpi(self):
        return self.__PI

c1 = Circulo(2.5)
print(c1.calcularArea())
print(c1.calcularPerimetro())
#print(c1.__radio) # Nos sale error debido al interprete de python

"""
    __radio python añade esto -> _Circulo__radio por temas de atributos o metodos con mismos nombres 

    """
# De esta forma no nos dara ningun error 
print (c1._Circulo__radio) 

"""
    Para acceder a un atributo o metodo privado usamos un metodo
    """
# ejemplo
print(c1.getpi())




