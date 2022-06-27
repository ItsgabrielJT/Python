
"""El scope es el alcance que tiene una variable en el programa"""

"""Scope global y local"""

x = 6 # Variable global

def funcion(y):
    print (x + y) # y es una variable local 

funcion(2)
print ("\n\n" + "-------------------")

"""palabra global"""

numero = 0

def comienza():
    global numero # Indicamos que la inofrmacion se guarde en la varible global
    numero = 9
    print (numero)

comienza()

def final():
    print (numero)

final()
print ("\n\n" + "-------------------")

"""palabra nonlocal"""

def prubea():
    a = 23
    def otrafuncion():
        nonlocal a # Especificamos que use la variable de la funcion prubea
        a = 2
        print (a)

    otrafuncion()
    print (a)

prubea()

