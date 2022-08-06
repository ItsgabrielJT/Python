
# Que es un dataframe
# Es una tabla compuesta por filas y columnas

import pandas as pd

personas = {
    "nombres": ["Joel", "Marco", "Andres"],
    "edades" : [12, 23, 45],
    "ciudades" : ["Quito", "Cuenca", "Quito"]
}

df = pd.DataFrame(personas)
print(df)

# Segundo metodo para crear dataframes
# Pasando una lista con listas

cabecera = ['marca', 'precio', 'modelo']
autoA = ['volvo', 12e3, 'copernico']
autoB = ['nissan', 20e3, 'ztrail']

df = pd.DataFrame([autoA, autoB], columns=cabecera)

# TErcer metodo 
# pasando varias listas

precios = [
    12e3,
    20e3,
    24e3,
    12e3
]

nombres = [
    'nissan',
    'chevrolet',
    'hunday',
    'volvo'
]

disponibilidad = [
    True,
    True,
    False,
    False
]

df = pd.DataFrame(
    list(zip(nombres, precios, disponibilidad)),
    columns=['marca', 'precio', 'disponibilidad']
)


