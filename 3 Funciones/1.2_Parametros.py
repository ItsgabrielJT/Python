
numero = 23;

def suma (x): # Pasamos como parametro x
    print (x + 40)

suma(numero) #Pasamos como argumento numero

"""Parametos por defecto"""

def mostrar_mensaje (nombre = "Joel"): # Al asignarle un valor se hace un paramtro por defecto
    print ("Que tal ? " + nombre + " Como estas")

mostrar_mensaje() # Se usa el parametro por defecto en la funcion
mostrar_mensaje("Hector") # Usa el argumento que le hemos pasap

"""Numero de argmentos variable"""

def numeros (*values): #Guarda todo slos argumentos como una tupla
    print (values)

print (numeros(12, 23, 45, 54)) #Recibe cualquier cantidad de augumentos

""" Dicccionarios como argumentos"""

def alumnos (aprobados, **cursos): #Con los dos asteriscos especificamos que es un diccionrio
    total = 0
    for alumno in cursos.values():
        total += alumno
    return aprobados * 100 / total

# Podemos pasar directamente los elemntos o creamos un diccionario
porcentaje = alumnos (50, A = 20, B = 40, C = 30) #Pasamos los elemntos del diccionario
print ("El porcentake de aprobados es: " + str(porcentaje))

"""Parametros no nombrados"""

def no_nombrado (a, b, /, c): # Lo que sigue de la barra son parametros nombredos
    print (a, b, c)

# Respetamos el orden de los parametros al pasar los argumentos
no_nombrado(12, 34, c = 30) #especificamos que dato recibe el parametro nombrado

