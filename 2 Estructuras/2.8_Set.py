# 1.- Que es set
# Son conjuntos de datos que no tienen un orden, es decir un indice por el cual acceder a sus elemetnos
# Cada uno de sus elementos son unicos, no pueden haber dos iguales

# 2.- Que es frozenset
# Es tambien cun conjutno de datos, la difrecnia con set es que esta es inmutable

# 3.- Formas de crear un set

# Mediante el contructor de la clase, pasandole objetos iterables (listas, tuplas, diccionarios, cadenas)
s = set([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Mediante dos llaves
a = {1, 2, 4, 6, 8, 20}

# Para crear un conjunto vacio, usamos el contructor
# no usamos las llaves porque si no creamos un diccionario vacio
c = set()

# 4.- Acceder a los elementos
# Como sabemos set es un conjunto desordenado pero podemos iterar con for para cceder a sus datos
# Hay que fijarse que se imprimen de orden distinto al que proporicionamos

for n in s:
    print (s)

# 5.- Anadir elementos al conjunto
# add = anade un uncio elementos
# update = anade todos los elemtnos que le pasemos
# Ambos metodos no agregan valores repetidos

s.add(20)
# s.update(1)

# 6.- Eliminar un elemento del conjunto
# discard() y remove(), eliminan un elmento dado, la difrencia es que el segundo lanza un excepcion si el elemnto no existe y el primero no
# pop() devulve un elemnto aleatorio del conjunto despues de eliminarlo
# clear() elimina todos los elemtnos de un conjnto

a.discard(10)
a.remove(2)
a.pop()
a.clear()

# 7.- Operadores de conjuntos 
# Tenemos los operadores que no cambian los elelemtnos del conjunto original
# .union(), une todos los elementos repetidos y los nuevos
# .intersection(), une todos los elemrntos que estan en ambos conjuntos
# .difference(), coge los elemtnos del conjunto A que no estan en B
# .symmetric_difference(), une los elementos que no estan repetidos en ambos conjuntos

a = set([1 ,2 ,3 ,4 ,5, 6, 7, 8, 9])
b =set([10, 1, 2, 3, 11, 21, 55, 6, 8])

print(a.union(b))
print(a)
print(a.intersection(b))
print(a)
print(a.difference(b))
print(a)
print(a.symmetric_difference(b))
print(a)

# Tambien tenemos los operadores que pueden modificar el conjunto original




