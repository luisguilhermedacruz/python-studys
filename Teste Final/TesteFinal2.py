# --*-- coding:utf-8 --*--

## ex8

numeros = [0,1,2,3,4,5,6,7,9,10,11,12]
numerosPares = []

for p in numeros:
    if p % 2 == 0:
        numerosPares.append(p)

print(numerosPares)