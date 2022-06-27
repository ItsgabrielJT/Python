# Los diccionarios son de tipo mutable por lo tanto sus elemtnos pueden ser cambiados
# Los diccionarios tienen una clave y valor 
# Las claves de los diccionarios no pueden estar repitidos pero los valores si

# 1.- Definir un diccionario
    # 1.1- Definiendo un diccnario con elementos

numeros = {"A": 3, "B": 4.35, "C": 5, "D": 5} # Clave :valor 
print(numeros) # Muestra todos los elemtnos del diccionario

    # 1.2- Definiendo un diccionario vacio

diccionario = dict() # Usando la palabra dict 

# 2.- Mostrar elemntos especificos
# Para cuando queremos que el diccionario nos muestre algo especifico hacemos lo siguiente

print(numeros.keys()) # Muestra solo los claves
print(numeros.values()) # Muestra todos los valores
print(numeros["A"]) # Muestra el valor de la clave "A"

# 3.- Modificar elementos del Diccionario
    # 3.1- Agregar elemtnos a un diccionario
    # De esta forma agregamos una clave y un valor

diccionario["Joel"] = 34
print (diccionario)

    # 3.2- Modificar elemntos

numeros["B"] = 75
print (numeros)

# 4.- Metodos con los diccionarios

diccionario.clear() # Elimina todos los elemntos del diccionario
print (diccionario)










