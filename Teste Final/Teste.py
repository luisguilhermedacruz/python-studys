numeroEscolhido = int(input("Digite um número"))

if numeroEscolhido % 2 == 0:
    print("PAR!")
else:
    print("IMPAR!")

if numeroEscolhido % 5 == 0:
    print("Multiplo de 5!")
else:
    print("Nao multiplo de 5")


numeros = [3,7,12,15,22,30,41]

numerosMaiorQue10 = []

for n in numeros:
   if n > 10:
    numerosMaiorQue10.append(n)

print(sum(numeros))
print(sum(numerosMaiorQue10))

