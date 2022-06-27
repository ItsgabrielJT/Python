
cadenas = [20, 7, 6, 2, 8, 10, 0]

nuevo = 0
pos = 0 
N = len(cadenas)

for i in range(1, N):
    nuevo = cadenas[i]
    pos = 0
    while pos < i and not(cadenas[pos] > nuevo):
        pos += 1

    for j in range(i, pos):
        cadenas[j] = cadenas[j - 1]

    cadenas[pos] = nuevo

print(cadenas)






