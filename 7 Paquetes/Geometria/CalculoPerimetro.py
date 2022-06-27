import math

class Perimetro:
    def __init__(self):
        pass

    def perimetroCuadrado(self, lado):
        return lado * 4

    def perimetroCirculo(self, radio):
        return math.pi * radio * 2

    def perimetroTriangulo(self, base, altura):
        return base * altura

    