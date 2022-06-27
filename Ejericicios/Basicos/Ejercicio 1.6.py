
cadena = []

def guardarLista():
    nombre = input("Ingrese los nombres: ")
    global cadena
    cadena = nombre.split() # Por defecto guarda los nombres desoues de un espacio

guardarLista()

def ultimaLetra(cadena, pos):    
    palabra = cadena[pos]
    inicio = len(palabra) - 1
    final = len(palabra)
    return str(palabra[inicio:final])


def aumentarLetra(cadena):
    contador = 0
    while contador < len(cadena):
        if ultimaLetra(cadena, contador) == "a":
            print (cadena[contador] + "s")
        elif ultimaLetra(cadena, contador) == "e":
            print (cadena[contador] + "s")
        elif ultimaLetra(cadena, contador) == "i":
            print (cadena[contador] + "s")
        elif ultimaLetra(cadena, contador) == "o":
            print (cadena[contador] + "s")
        elif ultimaLetra(cadena, contador) == "u":
            print (cadena[contador] + "s")            
        else:
            print (cadena[contador] + "es")           
        contador += 1 

aumentarLetra(cadena)






