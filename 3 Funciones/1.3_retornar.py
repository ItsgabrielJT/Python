
def mi_resultado():
    x = 30
    y = 40
    return x + y

resultado = mi_resultado()
print ("El sesultao es: " + str(resultado))

"""Funciones que retornan varios valores"""

def suma_resta (a, b):
    return a + b, a - b

suma, resta = suma_resta(10, 30)
print ("Los resultados son: \nSuma: " + str(suma) + "\nResta: " + str(resta))



