''' Dada una cadena de números,comparar los dígitos e indicar cuantos de ellos son pares y cuantos
son impares.C="isa,4,w,5,6,7,8,isa" '''

C="isa,4,w,5,6,7,8,isa"

numeros = C.split(',')

a, *b, c =  numeros

print(b)

b.remove('w')

lista = []

try:
    lista = list(map(int, b))
except ValueError as e:
    raise e

print (lista)

i = 0
j = 0
for n in lista:
    if n % 2 == 0:
        i += 1        
    else:
        j += 1

print(f"{i}, {j}")



