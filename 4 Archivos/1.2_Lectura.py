# PRIMERA FORMA
fichero = open('./archivo.txt', 'rt', encoding='utf-8') # Con encoding leemos caracteres especiales
primera_linea = fichero.readline() # Tambien lee los espacios y saltos de linea
print (primera_linea)

#Leee la lineas faltantes
todas_lineas = fichero.readlines() # Lee todas las lineas como una lista
print (todas_lineas)

fichero.close() # Siempre debemos cerrar el archivo

# SEGUNDA FORMA
"""
with open ("archivo.txt", 'r') as archivo: #Por defecto ya viene la r asi que podemos quitarla
    for linea in archivo:
        print ("----- Esrudiante ------")
        print (linea) # la variable linea guarda lo del archivo """

