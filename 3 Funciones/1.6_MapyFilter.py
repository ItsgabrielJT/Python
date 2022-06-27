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

# Forma de iterar una lista sin la funcion

for correo in emails:
    if '@' in correo:
        print (f"El email {correo} es valido")
    else:
        print (f"El email {correo} es invalido")

