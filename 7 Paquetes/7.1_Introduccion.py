
# Los paquetes en Python son conjuntos de modulos dentro de un mismo directorio
# Es buena parctica de programacion crear el __init__.py 

# 1.- Forma para importar paquetes
    # La sintaxis para esto es:
    # import paquete.modulo 

import Geometria.CalculoPerimetro # Especificamos el paquete Geometria qur contiene dos modulos
figuras = Geometria.CalculoPerimetro.Perimetro()
print (figuras.perimetroCirculo(12))

# 2.- Forma de acortar todo la importacion
    # La sintaxis para esto es:
    # import paquete.modulo as CP

import Geometria.CalculosAreas as CP
print (CP.areaCuadrado(5))

# 3.- Especificar un elemento del paquete
    # La sintaxis para esto es:
    # from paquete.modulo import elemento

from Geometria.CalculosAreas import areaCirculo
print (areaCirculo(23)) # Hacemos uso del unico elemento que importamos

# 4.- Combinacion de los casos 2 y 3
    # La sintaxis para esto es:
    # from paquete.modulo import elemento as nombre_cualquiera

from Geometria.CalculosAreas import areaTriangulo as triangulo
# Aqui estamos importando la funcion areaTriangulo y la llamos triangulo
print (triangulo(12, 5))

