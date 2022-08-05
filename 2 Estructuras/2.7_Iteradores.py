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

# 4.- Iterar sobre dos secuencias simultaneamente
# La funcion zip recorre sobre ambas listas simultaneamente
numero = [1, 2, 3, 4, 5]
vocales = ["a", "b", "c", "d", "e"]

for num, let in zip(numero, vocales):    
    print (num, let)

# 5.- Iterar sin la necesidad de hacer tu propio contador

# Antes tendriamos que hacer esto para saber cuantas evces iteramos osbre una lista
contador = 1
for n in vocales:
    print (contador, n)
    contador += 1

# La funcion enumerate
# Toma un iterable y un valor inicial(opcional)
# Si omites el valor inicial empieza en cero

for cont, a in enumerate(vocales, 1):
    print(cont, a)

# Asigancion de variables a iteradores
# Nosotrsd pofmo seprar un lista de su primer y ultimo elemtno en la lista
edades = [12, 23, 34, 45, 34, 23]

a, *b, c = edades
print(a)
print(b)
print (c)  


 

