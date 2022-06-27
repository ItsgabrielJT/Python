# 1.- Argumentos Arbitrarios
# Se utilizan cuando no sabemos la cantidad de parametros que va a recibir la funcion
# *args, es una convencion que nos señala que la funcion recibira N parametros
# Todo se guarda como una lista

def maximo(*args):
    maximo = args[0]
    for numero in args[1:]:
        if numero > maximo:
            maximo = numero
    return maximo

print (maximo(12, 34, -10, 35, -100, 2, 456, 23, 45))
print ("\n--------------------------------------------------------------------")

# 2.- Keyword Arguments
# Podemos pasar los argumentos de forma que el orden sea indiferente

def cargarPersonaje(nombre, raza, clase):
    print (f"{nombre.upper()} es un {clase} de raza {raza}")

cargarPersonaje(raza = "Humano", nombre = "Zelda", clase = "Guerrero")
print ("\n--------------------------------------------------------------------")

# 3.- Keyword Arguments Arbitrarios
# Las usamos cuando no sabemos cuantos argumentos de palabras claves vamos a recibir
# **kwargs, es una convencion
# Al usar lod dos asteriiscos se guardan los argumentos como un diccionario

def imprimir(**kwargs):
    print("Los atributos del personaje son: ")
    for clave, valor in kwargs.items():
        print (f"{clave} -------> {valor}")

imprimir (nombre = "leonidas", clase = "Guerrero", raza = "Humano", poder = 150)
print ("\n--------------------------------------------------------------------")





