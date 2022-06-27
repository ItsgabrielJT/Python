
# Desarrolar una funcion clasificar que reciba una lista de cadenas donde cada cadena
# es el nombre y el apellido de una persona y clasifique dichas personas por su apellido

# Clasifique en un diccionario todos los apellidos de las personas, guardando para cada 
# apellido una lista de los nombres de las personas


def clasificar (*lista):    
    personas = dict()
    nombreslista = list()
    for nombres in lista:
        nombre, apellido = nombres.split()
    return personas

print (clasificar("Joel Tates", "Henry Tates", "Msri Asimbaya", "Vero Asimbaya"))

