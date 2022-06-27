# La biblioteca numpy se utiiza para usar arreglos y matrices en python

import numpy as np # Simplificamos la palabra numpy por np

# 1.- Creacion de un Array
    # invocamos la biblioteca numpy con su alias np para declarar el metodo array.

vector = np.array([1, 2, 3, 4, 5])
print (vector)

# 2.- Imprimir o acceder a los elemtnos del array
    # Usamos los corchetes con la posicion del elemento

print (vector[0])
print (vector[2])
print (vector[4])

# 3.- Transformar los tipos de datos
    # utilizamos el metodo astype para transformar los datos de un array al tipo de dato
    # que queramos.

print (vector.astype(str))

# 4.- Operaciones con vectores
    # Todas las operacione se hacen con las mismas posiciones del ambos arreglos por ejemplo:
    # 5 + 3, 6 - 4; estos son elemtnos de los arrays a y b de abajo y que corresponden a las 
    # posiciones 0 y 1 de ambos arrays

a = np.array([5, 6, 7, 8, 9, 10])
b = np.array([3, 4, 1, 10, 5, 2])
print (a + b) 
print (a - b) 
print (a * b) 
print (a > b)

# 5.- Metodos con arrays

vector2 = np.array([12, 34, 0, 120, 23])
print (vector2.argmax()) # Retorna la posicion del maximo elemtno

print (vector2.sum()) # Suma todos los elemtnos
print (vector2.prod()) # Multiplica todos los elemtnos





