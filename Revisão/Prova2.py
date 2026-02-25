def calcularDesconto(preco, desconto =  10):
    return preco * (1 - desconto/100)

print(calcularDesconto(100))
print(calcularDesconto(200, 20))

carro = {"marca": "Ford", "ano": 2020, "preco": 85000}

if carro["preco"] > 50000:
    carro["caro"] = True
else:
    carro["caro"] = False


print(carro)
print(carro.get("cor", "não informado!"))

maiorNota = []

alunos = [
    {"nome": "Ana", "nota": 8},
    {"nome": "Pedro", "nota": 5},
    {"nome": "Julia", "nota": 9}
]

maiorNota = 0
alunoMaiorNota = []

for m in alunos:
    if m["nota"] > maiorNota:
        maiorNota = m["nota"]
        alunoMaiorNota = m["nome"]

print(f"O aluno com a maior nota é {alunoMaiorNota} com a nota de {maiorNota}")

for chaves, valor in carro.items():
    print(f"{chaves}: {valor}")