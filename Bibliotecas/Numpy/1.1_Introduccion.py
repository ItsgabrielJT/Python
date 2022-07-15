# Numpy
# Es un paquete para computo cientifico
# Los utilizamos para crear vectores y matrices (ndarray)
# Podemos hacer calculos matematicos y cientificos
# Es rapido y eficiente

import numpy as np

# 1.- Formas de crear arreglos
# A partir de un lista

numeros_lista = [1, 2, 3, 4, 5, 6]
numeros_array = np.array(numeros_lista)
print (numeros_array)

# Crear arreglos de dos dimensiones
numeros_dos = np.array([1, 3, 4], [12, 6, 7])
print (numeros_dos)

# Crear arreglos con tipos de datos definidos
numeros_tres = np.array([23, 5, 4], dtype='int16')
print (numeros_dos)

# 2.- Crear arreglos inicializados
# Inicializamos un arreglo con 0

ceros = np.zeros(10)
print (ceros)

# 3.- Crear arreglos con numeros
# Agregamos numeros del 0 al 10

inicio = np.arange(10)
print (inicio)

# Inica desde 0 =, termina antes dek 29 y va a r=ir de dos en dos
pares = np.arange(0,20, 2)
print (pares)

# Para crear arreglos bidimensionales
# Crea un arreglo bidimensional de dos filas y cinco columnas
pares.reshape(2 , 5)
print (pares)

# 4.- Operaiones entre arrays

impares = pares + 1
print (impares) # Suma a todos los elemtnos 1

impares * 100
impares - pares
impares / pares # Python define la division como cero de forma indefinida

# 5.- Metodos con operaciones

# Suma todos loes slemetnos del arreglo
impares.sum() 

# Saca el promedio dek arregki
impares.mean()

# Saca la varianza del arreglo
impares.var()

# Ordenar de menor a mayor un arreglo
notas = np.array([23, 34, 0, 1, 200, 45, 54, 12, 5, 23, 50])
np.sort(notas)

# Odeerna de mayor a menor
-np.sort(-notas)

# Obtener las dimensiones de un arreglo
print (pares.ndim)
print (notas.ndim)

# Obetner el tamano del arreglo 
print (pares.size)

# Llenar todo un arreglo de unos
unos = np.ones((4, 2), dtype='float32')
print (unos)

# LLenar todo un arreglo con un mismo numero
cincos = np.full((2,2), 5)
print (cincos)

# LLenar un arreglo de forma ramdon
random = np.random.rand(4,2)
print (random)

# 6.- Forma de seleccionar elemtnos

A = np.arange(0, 20, 2).reshape(2, 5)
print (A[0,0]) # Cogemos una fila y una columna

# para sekecionar todo una fila
print (A[1, :])

# Trabaajr con fikters
notas[notas < 20]  # Guarda los elementos que son menores que 20 (dentro de los corchetes se cumple la codndicion)
print (notas)
 
# 7.- Formas de copiar un arreglo
# Cunado asifnamos directamente el arreglo, estamos redirigiendo a esa variable a la misma direccion de memoira
# Que tiene el arreglo original
# POr tanto cuando cambiamos un elemento del arreglo nuevo tambien fecta al arreglo original

f = np.array([1, 3, 4])
g = f
g[0] = 100
print (f)

















