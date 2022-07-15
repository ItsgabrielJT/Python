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

palabra2 = "Como estas"
reves = palabra2.__reversed__()

print(reves.__next__())
print(reves.__next__())
print(reves.__next__())
print(reves.__next__())

# Iterar sobre dos secuencias simultaneamente
# LA funcion zip recorre sobre ambas listas simultaneamente
numero = [1, 2, 3, 4, 5]
vocales = ["a", "b", "c", "d", "e"]

for num, let in zip(numero, vocales):    
    print (num, let)


