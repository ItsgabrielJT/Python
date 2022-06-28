# DEcoradores
# Nos ayudan a modificar el comportamiento de una funcion

# 1.- Funciones como obejtos
# Las funciones pueden ser usadas como obejtos, es decir que no se ejecutan
# Las funciones al ser definidads con parentesis estamos ejecutandolas de forma automatica
# Las funciones son intancias de la clase objeto

def funcionExterna(nombre):

    def funionInterna():
       print("Estoy adentro de la funcion" + nombre)

    return funionInterna # Estamos retornando la funcion como un objetos

def segundaFuncionExterna(nombre):

    def segundaFunionInterna():
        print("Estoy adentro de la funcion" + nombre)

    return segundaFunionInterna() # Estamos retornando la ejecucion de la funcion

funcionExterna("Joel") 
segundaFuncionExterna("Marina")

# Instancias con funciones
# Como las funciones puden ser tratadas como obejtos podemos asiganarl una variable y esa variable instancia esa funcion

primero = funcionExterna("Lucas") # Instanciando una funcion 
primero() # Ejecutando la funcion 


# 2. -Funciones como argumentos
# LAs fucniones tambien pueden ser usadas como argumentos

from datetime import datetime

def fecha():
    print(datetime.today().strftime("%d-%m-%y"))

def hora():
    print(datetime.now().strftime("%H:%M:%S"))

def functEnvolotorio(funcionInt):
    def funcNucleo():
        print("Inicio")
        funcionInt()
        print("Fin")

    return funcNucleo

mostrarHora = functEnvolotorio(hora)

# 3.- DEcoradores
# Ejecutan una funcion que este como argumento

@functEnvolotorio
def mensaje():
    print("Hola como estas")























