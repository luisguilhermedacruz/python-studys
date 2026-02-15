## 1 

numero = int(input(f"Digite um numero!"))

if numero < 0:
    print("Número negativo!")
elif numero % 2 == 0:
    print(f"Número par!")
else:
    print(f"Número Impar!")


numeros = [3,7,12,15,22,30,41]

maiorDeTodos = numeros[0]

maior_que_dez = []

for m in numeros:
    if m > 10:
        maior_que_dez.append(m)

for i in numeros:
    if maiorDeTodos < i:
        maiorDeTodos = i

somaNumeros = sum(maior_que_dez)

print(maior_que_dez)
print(somaNumeros)
print(maiorDeTodos)

##2

notas = [6,8,7]

def calcular_media(notas):
    soma = sum(notas)
    media = soma / len(notas)
    situacao = ""

    if media >= 7:
        situacao = "Aprovado!"
    elif media >= 5 and media < 7:
        situacao = "Em recuperacao!"
    else:
        situacao = "Reprovado"

    return media, situacao

print(calcular_media(notas))




##3

faturamento = float(input("Quanto você faturou hoje?"))
combustivel = float(input("Quanto gastou de combustível hoje?"))

lucroLiquido = faturamento-combustivel
meta_minima = 300
meta_cheia = 400

if lucroLiquido >= meta_minima and lucroLiquido < meta_cheia:
    print(f"Você atingiu a meta minima de 300, está bom, mas ficou faltando {meta_cheia-lucroLiquido} para a meta cheia! Mesmo assim, god job!")
elif lucroLiquido >= meta_cheia:
    print("Excelente job, meu jovem! Meta batida!")
else:
    print(f"Precisa melhorar e ainda falta: {meta_minima - lucroLiquido}")


