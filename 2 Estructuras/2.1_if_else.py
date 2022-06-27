temperatura = int( input ("Ingrese la temperatura: ") )

"""Condicion simple"""

if temperatura < 15:
    print ( "Frio" )
else:
    print ( "Calor" )

"""Condicion doble"""

if temperatura > 25:
    print ( "Ponte solo camiseta" )
elif temperatura == 35:
    print ( "Anda con ropa normal" )
else:
    print ( "Anda con mucha ropa")