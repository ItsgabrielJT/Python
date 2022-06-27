"""
    Queremos comparar el tiempo en que tarda en sumas todos los elemtnos de una lista de elemntos enteros con ayuda
    de un bucle for y while ademas de esto el resultado se guardara en un archivo

    """

import time, random

lista = []
for x in range(50000):
    lista.append(random.randint(0, 150000)) # rnadint añade numeroas enteros a la lista de rango 0 a 150000

archivo = open('./tiempos.txt', 'wt', encoding = 'utf-8')

for x in range(100):
    sumatoria = 0
    comenzar_tiempo = time.time() # retorna tiempo actual en segundo con decimales de precision
    for numero in lista:
        sumatoria += numero
    tiempo_bucle_for = time.time() - comenzar_tiempo# tiempo que se hizo en el bucle

    pos = 0
    sumatoria2 = 0
    comenzar_tiempo = time.time()
    while pos < len(lista):
        sumatoria2 += lista[pos]
        pos += 1
    tiempo_bucle_while = time.time() - comenzar_tiempo

    archivo.write(f"{tiempo_bucle_for};{tiempo_bucle_while}\n")

archivo.close()

archivo = open('./tiempos.txt', encoding = 'utf-8') # Solo lectura del archivo
media_for = 0
media_while = 0
muestras = 0

for linea in archivo.readlines(): # Se guarda como una lista
    linea.replace('\n', "") # Elimansmos los saltos de lineas
    tiempo_for, tiempo_while = linea.split(";") #Separamos la lista en dos posiciones 
    media_for += float(tiempo_for)
    media_while += float(tiempo_while)
    muestras += 1

print (f"Tiempo for: {media_for / muestras:.3f}, Tiempo while: {media_while / muestras:.3f}")