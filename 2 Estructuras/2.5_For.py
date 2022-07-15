
for i in range(4): #incia con 0 por defecto y termina siempre restando uno al valor de los parentesis
    print(i)

print ("\n")

for j in range(1,5): #inicia desde 1
    print (j)

print ("\n")

for k in range(1,7,2): # inciia en 1 y va sumando de dos en dos
    print (k)

print ("\n")

"""Iteracion en estructura de datos"""

numeros = [1, 2, 3, 4, 5]
for num in numeros: # Iterando sobre listas
    print (num)

print ("\n")

letras = ('A', 'B', 'C', 'D') # iterando sobre tuplas
for let in letras:
    print (let)

print ("\n")

diccionario = {"a": 1, "b": 2, "c": 3}
for clave in diccionario: 
    print (clave) # Nos muestra las claves del diccionario

print ("\n")

for valor in diccionario.values(): # Nos retorna los valores
    print (valor)

print ("\n")

for clave, valor in diccionario.items(): # Nos retorna los pares
    print (clave, valor)

# Clausla else dentro del for
# Esta clausula se ejecuta cuando no se encuntra un break o cuando no se ejcuta ese break;

lista = [3, 5, 9, 7]
for num in lista:
    if num % 2 == 0: 
        print("Se encontro un par")
        break;
    else:
        print(num)
else:
    print("No se encontro ningun numero par")









