
# Que son las comprehendios 
# Son estrucutras de datos que permiten generan secuencias a partir de otras secuencias

# Ejemplo de crompenhension con listas
numeros = list(range(50))
pares = [par for par in numeros if par % 2 == 0]
print (pares)

# Ejemplo de comprenhensions con disccionarios
userid = [1, 2, 3]
names = ["Joel", "Gabriel", "Ana"]
students = {uid: name for uid, name in zip(userid, names)}
print (students)


