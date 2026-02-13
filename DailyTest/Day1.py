numeros = [5,3,8,3,9,1,1]

maior = numeros[0]
menor = numeros [0]

contaRepeticaoMaior = 0
contaRepeticaoMenor = 0

for n in numeros:
    if n > maior:
        maior = n
        if maior == n:
            contaRepeticaoMaior += 1
    if n < menor:
        menor = n
        if menor == n:
            contaRepeticaoMenor += 1


print(f"O maior número é: {maior} e ele se repete por {contaRepeticaoMaior}")
print(f"O maior número é: {menor} e ele se repete por {contaRepeticaoMenor}")




## EU NAO SEI SABER QUAL MAIOR NUMERO.     


