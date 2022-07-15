# Ejericcio de decoradores en python
# Del archivo de decoradores, completar el ejemplo del caso 4
# Retornar el mismo numero delimitado por el ususrio al realizar cierto numero de multiplicaciones
# tambien introducidas por el ususrio, 
# Ejemplo multiplicar(1, 2, 4, 5, 6, 50)
# ----> 50 Porque la multipllicacion excedio el limite y el limite era 50

def operarConPares(operacion):
    def wrapper (*args, **kwargs):
        soloPAres = list(filter(lambda num: num % 2 == 0, args))
        resultado = operacion(*soloPAres, **kwargs) 
        print(f"El resultado es {resultado}")
    return wrapper

# Solucion mia
"""@operarConPares
def multiplicar(*args, **kwargs):
    ac = 1
    limit = list(kwargs.values())
    for num in args:
        ac *= num
    if ac > limit[0]:
        return limit[0]
    else:
        return ac
        """
# Solucion del video
@operarConPares
def multiplicar(*args, **kwargs):
    ac = 1
    for num in args:
        ac *= num
    if "max" in kwargs.keys():
        return min(kwargs["max"], ac) # Compara y nos retorna el minimo
    # Si sejecuta el return anterior ya no ejecuta el de aqui abajo
    return ac

multiplicar(1, 2, 3, 4, 5, 6, 7, 8, max = 50)

 

