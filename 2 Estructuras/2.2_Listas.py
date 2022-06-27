"""Caracteristicas de las listas"""
#El orden de las listas no pueden ser modificadas, solo se modifican con metodos de listas
#Las lstas son del tipo mutable es decir que pueder ser modificafdas
# Usamos simepre corchetes para guardar los elementos

numeros = [1, 20, 0, 4, 16, 0] # Usa indices desde 0

print (numeros[0]) # ingresamos al primer elemento

"""Obtener la longitud de la lista"""

print(len(numeros))

"""Agregar elementos a la lista"""

numeros.append(23) # Se agrega al final de la lista
print (numeros)

numeros.insert(0, 10) # insertamos en el indice 0 el elemento 10
print (numeros)

"""Eliminar elemntos"""

numeros.remove(4) # Especificamos el elemento
print (numeros)

"""Econstrar un elemento o posicion"""

10 in numeros # elemtno que buscamos, nos retorna un boleano

numeros.index(20) # retorna la posicion del elemento 

"""Cambiar elemntos""" 
# Podemos hacer esto gracias a que las listas son mutables

numeros[2] = 15
print (numeros)

"""Metodos de listas"""

numeros.count(0) #nos deja ver cuantas veces se repite un elemnto

negativos = [-1, -2, -3, -5]
numeros.extend(negativos) #nos deja agregar otra lista dentro de numeros
print(numeros)

numeros.pop(0) # Remueve y retorna un elemento de lista
print(numeros)

numeros.reverse() # Reversa el orden de la lsita
print(numeros)

numeros.sort() #ordena la lista sin especifircar el orden (Por defecto de form ascendente)
print(numeros)
numeros.sort(reverse = True) #ordena la lista sin especifircar el orden (Por defecto de form descendente)
print(numeros)

"""Iterar entres lista"""

lista = [1, 2, 3, 4, 5]
iterador = iter(lista)
#print(iterador) # Nos muestra que objeto esta iterando
#print(iterador.__next__()) # nos muestra un elemento de la lista
#print(iterador.__next__()) # nos muestra el proximo elemnto de la lista

contador = 0

while contador < 5:
    print (iterador.__next__()) # Obtenemos todos los valores del objeto
    contador += 1

print ("\n")
# SEGUNDA FROMA PARA ITERAR

pasador = lista.__iter__();

contador = 0

while contador < 5:
    print (pasador.__next__()) # Obtenemos todos los valores del objeto
    contador += 1