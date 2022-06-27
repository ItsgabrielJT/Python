
"""
    Crear una fucnion que retorne el numero ms grande de la comparacion entre dos numeros, que retorne un false
    y un mensaje error cuando se compruebe que los numeros no son de tipo int o float
"""

num1 = int(input("Ingrese el primer numero: "))
num2 = int(input("Ingrese el segundo numero: "))

def maximo (numero1, numero2):
    if (type(numero1) == int or type(numero1) == float ) and (type(numero2) == int or type(numero2) == float):
        if numero1 == numero2:
            print ("Los dos numeros son iguales")
        elif numero1 > numero2:
            return numero1
        else:
            return numero2
    else:
        print ("Error !, el dato no es admitido")
        return False

comparacion = maximo (num1, num2)
if type(comparacion) != bool:
    print ("El mayor es: " + str(comparacion))
else:
    print ("EL resultado es: " + str(comparacion))




