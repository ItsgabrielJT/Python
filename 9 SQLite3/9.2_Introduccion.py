import sqlite3 as sql # Renombramos la libreria como sql

# Podemos hacer todo en la misma fucnion, solo se hace por separador para tener mayor legibilidad

def createDB():
    conn = sql.connect("Streamers.db") #Nombre de la BDD y la extension del archivo
    conn.commit()
    conn.close() # Cerramos la conexion


def creteTable():
    conn = sql.connect("Streamers.db")
    cursor = conn.cursor() # Intanciamos un objeto de la clase cursor
    cursor.execute ( # Las instrucciones sql son todas strings
        # Le pasamos un dogstring que es el uso de las trr comillas
        # Nombre del campo y tipo de dato
        # En el utlimo campo no colocamos comas
        """CREATE TABLE streamers ( 
            name text,
            followers integer,
            subs integer
        )""" 
    )
    conn.commit() # Es realizar los cmabios, es decir ejecutamos las instrucciones anteriores
    conn.close()

def insertRow(nombre, followers, subs):
    conn = sql.connect("Streamers.db")
    cursor = conn.cursor()
    # Estamos comuncandonos con la base de datos
    # INSERT, indica que queremos agregar algo a una tabla
    # INTO, indica a que tabla queremos agregar informacion
    # VALUES, son los valores de cada campo de la tabla
    # Los datos de tipo texto, los valores tienen que ir entre comillas
    instruccion = f"INSERT INTO streamers VALUES ('{nombre}', {followers}, {subs})" 
    cursor.execute (instruccion)
    conn.commit()
    conn.close()

def readRows():
    conn = sql.connect("Streamers.db")
    cursor = conn.cursor()
    # SELECT, significa que datos vamos a seleccionar
    # *, significa que queremos todos los datos
    # FROM, señalamos que tabla queremos 
    instruccion = f"SELECT * FROM streamers" 
    cursor.execute (instruccion) # Aqui ya se jecuta la instruccion de seleccionar
    # Est ainstruccion de abajp nos genera una lista y dentro de lla los datos se dividen en tuplas
    # Las tuplas contienen todos los campos de una misma fila
    datos = cursor.fetchall(); # Nos dvuelve una lista de todos los datos que ha seleccionado
    conn.commit()
    conn.close()
    print (datos)

def insertMuchRows(streamerList):
    conn = sql.connect("Streamers.db")
    cursor = conn.cursor()    
    # Las interrogamtes significa que vamos a pasar tres valores 
    instruccion = f"INSERT INTO streamers VALUES (?, ?, ?)" 
    # Execute many nos permite hacer varios insert
    cursor.executemany(instruccion, streamerList)
    conn.commit()
    conn.close()

def readOrdered(field):
    conn = sql.connect("Streamers.db")
    cursor = conn.cursor()
    #instruccion = f"SELECT * FROM streamers ORDER BY {field}" # Ordena de menor a mayor
    instruccion = f"SELECT * FROM streamers ORDER BY {field} DESC" # Ordena de mayor a menor
    cursor.execute (instruccion)
    datos = cursor.fetchall(); 
    conn.commit()
    conn.close()
    print (datos)

def search():
    conn = sql.connect("Streamers.db")
    cursor = conn.cursor()
    #WHERE, nos ayuda a localizar una elemtno de la tabla
    #instruccion = f"SELECT * FROM streamers WHERE name = 'Rubios'" #Buscamos el nombre
    instruccion = f"SELECT * FROM streamers WHERE name like 'rubios'" #Buscamos el nombre sin importar Mayus o Minus
    cursor.execute (instruccion)
    datos = cursor.fetchall(); 
    conn.commit()
    conn.close()
    print (datos)

def updateFields():
    conn = sql.connect("Streamers.db")
    cursor = conn.cursor()
    instruccion = f"UPDATE streamers SET followers = 12000000 WHERE name like 'auronplay'"
    cursor.execute (instruccion)
    conn.commit()
    conn.close()

def deleteRow():
    conn = sql.connect("Streamers.db")
    cursor = conn.cursor()
    instruccion = f"DELETE FROM streamers WHERE name = 'Fernanfloo'"
    cursor.execute (instruccion)
    conn.commit()
    conn.close()


if __name__ == "__main__":
    #createDB()
    creteTable()
    insertRow("Ibai", 70000000, 25000)
    insertRow("Rubius", 350000000, 34000)
    #readRows()
    streamers = [
        ("Rubios", 35000000, 34000),
        ("AuronPlay", 27000000, 10000),
        ("Fernanfloo", 3000000, 50000)
    ]
    #insertMuchRows(streamers)
    #readOrdered("subs")
    #search()
    #updateFields()
    #deleteRow()







