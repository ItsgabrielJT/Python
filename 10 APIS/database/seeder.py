from audioop import add
import sqlite3 as sql

DB_PATH = "C:/Users/gabrieljt/Desktop/Python/10 APIS/database/streamers.db" # Localizacion de i BDD

def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute (
        """
            CREATE TABLE streamers (
                nombre text,
                subs integer,
                followers integer 
            )
        """
    )
    conn.commit()
    conn.close()

def addValues():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    data = [
        ("axelcapo", 10000, 80000),
        ("ibai", 1210000, 10000),
        ("Fernanfloo", 32000, 234400),
        ("ElrubriosOMG", 2310000, 450000),
        ("auronplay", 2110000, 800000)
    ]
    cursor.executemany("""INSERT INTO streamers VALUES (?, ?, ?)""", data)
    conn.commit()
    conn.close()



if __name__ == '__main__':
    createDB()
    addValues()