
def mi_funcion(): # el nombre de las fnciones sigue escritura snake_case
    print ("Hokla mundo")

mi_funcion() # Relizamos la llamda de la funcion

"""Funciones lambda""" 

# Las funciones anonimas son buenas para crear procedimientos simples
# Forma convencional de definir una funcion
def mostrar_mensaje (a, b):
    print (a + b)

mostrar_mensaje(20, 40)

# lambda crea una funcion anonima
suma = lambda a, b: a + b # estas funciones no podemos crearlas un cuerpo
print (suma(20, 60))







