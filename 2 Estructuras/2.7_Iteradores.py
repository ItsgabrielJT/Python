# 1.- Que es un iterador
# Es un obejto que tiene la funcion next(), es decir que nos devlve el siguiente elemento de una lista

palabra = "Hola mundo"

# 2.- Formas de crear un iterador
letra = iter(palabra)
letra = palabra.__iter__()

# Nos imprime letra por letra
print(letra.__next__())
print(letra.__next__())
print(letra.__next__())
print(letra.__next__())

# 3.- Metrodos con iteradores
# Nos retorna letra por letra desde la ultima
reves = palabra.__reversed__()

print(reves.__next__())
print(reves.__next__())
print(reves.__next__())
print(reves.__next__())

