# Las funciones map y filter sirven para trabajar con objetos iterables 
# Los obejtos iterables pueden ser una lista, tupla, dicccionario
# Vienen incorporadas por defecto en Python

# 1.- Funcion Filter
# La la funcion filter le podemos pasar tambien como argumento otra funcion
# La sintaxis de la funcion filter es:
# filter(funcion, iterable)

emails = [
    "juan.pedro@gmail.com",
    "javierepn",
    "pedro@gmail.com",
    "magriver34"
]

emailsvalidos = []

# Forma de iterar una lista sin la funcion filter

"""
for correo in emails:
    if '@' in correo:
        print (f"El email {correo} es valido")
        emailsvalidos.append(correo)
    else:
        print (f"El email {correo} es invalido")

print(emailsvalidos)
"""

# Forma de iterar con la funcion filter

def evaluarEmail(email): # Filter se encaraga de iterar por eso colocamos un solo string
    return '@' in email

# Pasa elemetno por elemtno de l lista dentro de la funcion evaluarEmail

emailsvalidos = filter(evaluarEmail, emails) # Nos retarno obejetos iter, por tanto tenemos que usar next para ver sus valores
print(next(emailsvalidos))

emailsvalidos = list(filter(lambda email: '@' in email, emails)) # Hacemos lo mismo de arriba pero con lambdas y transformandolo a lista
print(emailsvalidos)


# 2.- Funcion Map
# Ejecuta la funcion usando como parametro la estructura iterable
# Nos devulve un objeto iterable y no se encarga de comprobar codsas
# La estructura de map(function, iterable)

palabras = ('hola', 'como', 'estas', 'hoy')
longitudes = list(map(lambda s: len(s), palabras))
print(longitudes)







