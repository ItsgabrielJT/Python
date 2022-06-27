#OPERADORES
numero1 = 9
numero2 = 2
resultado = numero1 * numero2

print (numero1 + numero2)
print (numero1 - numero2)
print (numero1 * numero2)
print (numero1 / numero2)#division real
print (numero1 // numero2)#division entera
print (numero1 % numero2)
print (numero1 ** numero2)#potenciacion

#el modulo te deja conseguir el ultimo numero de un digito
print (resultado % 10)#nos da el 8 porque es el ultimo numero

#prioridad de los operadores:
#Parentesis, Potencia, Multiplicacion y division, Suma y resultado
#operadores de igual precedencia se evalua de derecha a izquierda

#OPERADORES RELACIONALES
print (numero1 == numero2)
print (numero1 != numero2)
print (numero1 <= numero2)
print (numero1 >= numero2)
print (numero1 < numero2)
print (numero1 > numero2)
#la comparacion siempre te entrega un resultado tipo booleano

#OPERADORES LOGICOS
num1 = 12
num2 = 23
num3 = 45
num4 = 11

comparacion = num1 < num2
comparacio2 = num3 > num4

print (comparacion and comparacio2)
print (comparacion or comparacio2)
print (not comparacion) # negaciion


#OPERADORES DE INCREMENTO Y DECREMENTO
n = 4
n += 2 # se tracuce a n = n + 2
print (n)

n -= 2 # se traduce a n = n - 2
print (n)

