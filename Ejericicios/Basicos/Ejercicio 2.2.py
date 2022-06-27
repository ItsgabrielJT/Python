''' Dada una cadena de números,comparar los dígitos e indicar cuantos de ellos son pares y cuantos
son impares.C="isa,4,w,5,6,7,8,isa" '''


from sqlalchemy import values


C="isa,4,w,5,6,7,8,isa"

def compara(cadena):
    lista=cadena.split(',')
    
    for i in lista:
        if i == type(str) or i == type(int):
            aux = len(i)
            if i % 2 == 0:
                print("El número es par")
            else:
                print("El número es impar")

compara(C)
