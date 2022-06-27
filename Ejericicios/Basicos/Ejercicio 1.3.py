
print ("{:^40}".format("""
            ______________________________________________________________
           |                      O P C I O N E S                         |
           |______________________________________________________________|"""))

print ("{:^83}".format("1.- Regstrarse"))
print ("{:^86}".format("2.- Iniciar secion"))
print ("{:^78}".format("3.- Salir"))
print ("{:^87}".format("______________________________________________________________"))

try:
    opcion = int( input ("Opcion: "))
except ValueError: # Controla el error de entrada de tipo de dato diferente
    print ("Ese tipo de dato no es valido !, ingrese de nuevo...")
    opcion = int( input ("Opcion: "))

while (opcion != 3):
    if (opcion == 1):
        usuario = input ("Ingrese su nombre de usuario: ")
        contren = input ("Ingrese la contraseña: ")        
    elif (opcion == 2):
        print (usuario + contren)
    else:
        print ("Opcion no valida ! ingrese de nuevo")

    try:
        opcion = int( input ("Opcion: "))
    except ValueError: 
        print ("Ese tipo de dato no es valido !, ingrese de nuevo...")
        opcion = int( input ("Opcion: "))

print ("Ha salido correctamente")

