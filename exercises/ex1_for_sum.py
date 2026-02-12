# --*-- coding: utf-8 --*--

total = 0

## teste de somacom numeros pares de 1 a 20
for n in range(1, 21):
    if n % 2 == 0:
        total = total + n

print("A soma total dos números pares de 1 a 20 é:", total)

#teste de soma com numeros impares de 1 a 20

totalimpar = 0

for i in range(1,21):
    if i % 2 != 0:
        totalimpar = totalimpar + i

print("A soma de todos os números ímpares de 1 a 20 é:", totalimpar)

totalTriplo = 0

for t in range(1,21,3):
    totalTriplo = totalTriplo + t

print("A soma dos numeros de 3 em 3 de 1 a 20 é:" , totalTriplo)

