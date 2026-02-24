def somaTudo(lista):
    return sum(lista)

lista1 = list(range(100))

print(somaTudo(lista1))


def saudacao(nome, saudacao="Olá"):
    return f"{saudacao}, {nome}!"

print(saudacao("Elyda"))

aluno = {"nome": "Carlos", "nota": 7}

if (aluno.get("nota")) >= 6:
    aluno["aprovado"] = True
else:
    aluno["aprovado"] = False

print(aluno)


produtos = [
    {"nome": "caneta", "preco": 2.5},
    {"nome": "caderno", "preco": 15.0},
    {"nome": "mochila", "preco": 89.9}
]

maior_preco = 0
produtoMaisCaro = []

for m in produtos:
    if m ["preco"] > maior_preco:
        maior_preco = m ["preco"]
        produtoMaisCaro = m["nome"]
print(f"O produto mais caro é: {produtoMaisCaro} com valor de R${maior_preco}")

print(aluno.get("desconto", 0))

for chave, valor in aluno.items():
    print(f"{chave}:{valor}")