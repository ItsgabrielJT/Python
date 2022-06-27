numero = int (input ("Ingrese un numero: "))

print ( "\n", numero // 10000, "\t"
        ,(numero // 1000) % 10, "\t"
        ,(numero // 100) % 10, "\t"
        ,(numero // 10) % 10, "\t"
        ,numero % 10, "\t"           )