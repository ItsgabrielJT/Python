# Que es un dataset
# Es un conjuneto donde cada columna es una unica variable, es decir de un solo tipo de dato
# Sus filas representan a un unico elemento 

# LEeer archivos csv
import pandas as pd

# index nos quita la columna de indice generada por default de pandas
df = pd.read_csv("./data/avocado.csv", index_col=0)

# Cuando queramos ver en particular las primeras filas hacemos esto
df.head() # POr default nos muestra las cinco primeras filas
df.head(3) # NOs muestra las tres primeras filas


