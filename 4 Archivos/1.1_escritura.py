"""
    w = escribir (sobreescribe)
    r = leer (por defecto si no especificamos qur modo queremos)
    a = añadir
    x = crear un archivo con el nombre que queramos
    t = trabajar con archivos que solo tengan texto
    b = byte (para archivos como fotos)

    """

# PRIMERA FORMA
escritura = open('./demo.txt', 'w', encoding='utf-8')
escritura.write("Como estas xd \n") #leee solo una cadena de strings

lista_contenido = [
    'Hola como estas',
    'me la turboflipa',
    'estas enfermo bruce wayne'
]

lista_contenido = map(lambda linea: linea + '\n', lista_contenido)
print (lista_contenido)
escritura.writelines(lista_contenido)
escritura.close()

""" Creacion de un archivo """

try:
    fichero = open('./demo2.txt', 'x', encoding = 'utf-8')
    fichero.write("Como estas pinche ppuerca\n")
    # Muestra tru eo false apra saber si podemos escribir y leer en el archivo
    print (fichero.readable) 
    print (fichero.writable)
    fichero.close()
except FileExistsError:
    print ("Ese archivp ya est acreado, por eso no se puede crear")


# SEGUNDA FORMA
notas = {
    "Nora": 87,
    "Gino": 45,
    "Loretto": 56,
    "Talina": 45
}

with open ("archivo.txt", 'w') as archivo: # Estamos es cribindo en el archivo
    for nombre, nota in notas.items():
        archivo.write(nombre + " - " + str(nota)+ "\n")
