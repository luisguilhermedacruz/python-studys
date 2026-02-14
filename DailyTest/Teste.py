nota1 = float(input("Qual sua 1ª nota?"))
nota2 = float(input("Qual sua 2ª nota?"))
nota3 = float(input("Qual sua 3º nota?"))

notas = [nota1, nota2, nota3]
media = sum(notas)/ len(notas)
notaRecuperacao = 7 - media
maiorNota = 0

if media >= 7:
    print(f"Aluno aprovado!")
elif media >= 5 and media < 7:
    print(f"Aluno em recuperação! precisando de {notaRecuperacao} ")
else:
    print("Aluno reprovado por não atingir a nota minima!")

for n in notas:
    if n > maiorNota:
        maiorNota = n

print(maiorNota)

## 2 

numeros = [2,7,10,15,22,31,40]
contaPar = 0
contaImpar = 0
maiorNumero = 0
soma = sum(numeros)

for n in numeros:
    if n % 2 == 0:
        contaPar += 1
    else:
        contaImpar += 1

for n in numeros:
    if n > maiorNumero:
        maiorNumero = n

print(f"Numeros pares são: {contaPar}")
print(f"Numeros impares são: {contaImpar}")
print(soma)
print(maiorNumero)


    