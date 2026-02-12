## --*-- coding: utf-8 --*--

meu_dicionario = {"L":"LUIS", "B":"BRUNA", "S":"SANDRA"}

print(meu_dicionario["B"])

for chave in meu_dicionario:
    print(chave+":"+ meu_dicionario[chave])


## aqui retorna tupla
for i in meu_dicionario.items():
    print(i)