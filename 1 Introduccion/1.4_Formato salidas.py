#PRIMERA SALIDA DE DATOS
nombre = input("ingrese su nombre: ")
edad = input("Ingrese su edad: ")
print ("Su nmbre es: ")
print (nombre)
print ("Su edad es: ")
print (edad + "\n\n")

""" Formateo con .format() """

print ("mi nombres es: {} y mi tengo {} años\n\n".format(nombre, edad))
#en los corchetes ira el nombre y la edad en su respectivo orden


"""Formateo para aproximar decimalest"""

texto = "mi nombres es: {} y mi tengo {} años".format(nombre, edad)
#el punto format nos retorna el valor de una variable
print (texto)

#APROXIMAR DECIMALES
num1 = 2.60
num3 = 0.12
total = num1 + (num1 * num3)
print ("el precio final es {:.2f}\n\n". format(total))
# el ": .2f" se tiene que primero poner los dos puntos, luego el numero de decimales que queremos aproximar
# seguido de la letra f que significa float

"""Fromateo para centrar o acomodar datos"""

producto1= "Cpauchino"
valor1 = 2.60
iva = 0.12
total1 = valor1 + (valor1 * iva)

producto2= "Expreso"
valor2 = 1.10
iva = 0.12
total2 = valor2 + (valor2 * iva)

producto3= "Mocachino"
valor3 = 2.95
iva = 0.12
total3 = valor3 + (valor3 * iva)


# "^" simbolo para formato de salida centrado, el numero representa los espacios tanto de izquierda y derecha para que este centrado
#Ejemplo : **************PRODCUTO****************
#loa asteriscos representan los espacios

# "<" simbolo para formato de salida apegado a la derecha, el numero representa los espacios de derecha a izquierda
#Ejemplo: PRODUCTO***************************

# "<" simbolo para formato de salida apegado a la izquierda, el numero representa los espacios de izquierda a derecha
#Ejemplo: ***************************PRODUCTO

print ("{:^20} {:^20} {:^20}".format ("PRODCUTO", "VALOR SIN IVA", "TOTAL"))
print ("{:^20} {:^20} {:^20,.2f}".format (producto1, valor1, total1))
print ("{:^20} {:^20} {:^20,.2f}".format (producto2, valor2, total2))
print ("{:^20} {:^20} {:^20,.2f}".format (producto3, valor3, total3))
#no poner espacios despues de la coma dentro de los corchetes

"""Formateo con llaves"""

nombre = "Joel"
edad = 23

print (f"\n\nHola soy {nombre} y tengo {edad}\n\n") # El prefijo f transformo todo dato a str

"""Metodo para centrar cadenas"""

# en el primer argumento del metodo center ira los espacios que queremos pero toca tomar encuenta que sea mayor
# a la cadena que queremos centrar

print (nombre.center(4)) # no pasa nada porque la cadena tiene 4 elemtnos 
print (nombre.center(12)) # toma 8 espacios descontando los elemtnos de la cadena
print (nombre.center(12, '-')) # especificamos con que se rellena esos espacios vacios por defecto

"""Metodo para alinear cadenas a la izquierda"""

print (nombre.ljust(12, '-'))  # completa los espacios con ese cara ter




