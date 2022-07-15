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
mostrarHora()

# 3.- DEcoradores
# Ejecutan una funcion que este como argumento
# Aqui estamos pasando la funcion mensaje como parametro de la funcionEnvoltorio

@functEnvolotorio
def mensaje():
    print("Hola como estas")

mensaje()

# 4.- Multiples argumentos con DEcoradores


def sumar(*args, **kwargs):
    ac = 0
    for num in args:
        ac += num
    return ac

def operarConPares(operacion):
    def wrapper (*args, **kwargs):
        soloPAres = list(filter(lambda num: num % 2 == 0, args))
        resultado = operacion(*soloPAres, **kwargs) 
        print(f"El resultado es {resultado}")
    return wrapper

sumarPares = operarConPares(sumar)
sumarPares(1, 2, 3, 4, 5, 6)

@operarConPares
def multiplicar(*args, **kwargs):
    ac = 1
    for num in args:
        ac *= num
    return ac

multiplicar(1, 2, 3, 4, 5, 6)























