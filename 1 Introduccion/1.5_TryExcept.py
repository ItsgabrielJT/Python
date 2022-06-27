#Constrolar errores de entrada

"""Slo muestra un caso"""
"""
try:
    print (10/0)

except Exception as e:
    print ("Error de sistema: ", e) #La e muestra el tipo de error 
finally:
    ejecuta al final de todo el anterior proceso
"""

"""Multiuple errores"""

try:
    print (10/"d")
except TypeError as c: #Por tipo de dato equivcado
    print (c)
except ZeroDivisionError as e: # normalemnete se usa e porque signidica excepcion
    print (e)
else:
    #Si no ocurrio una excepcion
    #Ejecuta este codigo
    print ("Hola que tal")

