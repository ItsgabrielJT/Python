# Los modulos son archivos de Python que pueden contener funciones, clases y variables
# Usamos simepre el import para invocar un modulo

# 1.- Primera forma para usar las funciones o clases de un modulo
    # La sintaxis que se usa es:
    # modulo.funcion(args)

import math # Modulo con funciones matematicas
print (math.pow(9,2)) # Usando una funcion pow
print (math.pi) # Usando una constante 

# 2.- Asiganrle un alias al modulo
    # Podemos cambiar el nombre del modulo por el que nosotros queramos
    # La sintaxis para hacer esto es:
    # import modulo as nombre_alternativo

import math as matematicas # Cmabiamos el nombre math por matematicas
print (matematicas.pow(10, 2)) # Usamos el nombre por el que llamamos al modulo

# 3.- Para importar elementos exactos
    # Podemos solamente usar una fucnion, clase o variable exacta del modulo
    # De esta forma no invocamos todos sus elementos
    # La sintaxis para esto es:
    # from modulo import funcion

from math import pow # Solo invocamos la funcion pow
print (matematicas.pow(6, 3))

# 4.- Modulos sin uso de su nombre
    # De esta forma ya no necesitamos usar el nombre del modulo seguido del elemento que queramos
    # No sayuda a usar drectamente las funciones, clases o variables
    # La sintaxis para esto es:
    # from modulo import *

from math import * # El asteriusco importa todo lo del modulo
print (pow(4, 3))




