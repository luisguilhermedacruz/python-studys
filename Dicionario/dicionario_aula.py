def compara_idade(pessoas: dict[str, int]) -> tuple[str, int]:
    soma = sum(pessoas.values())
    media = soma / len(pessoas)

    maior_idade = max(pessoas, key=pessoas.get)
    
    return maior_idade, media

pessoas = {
    "LUIS": 31,
    "ELYDA": 29,
    "GAEL": 3
}

maior, media = compara_idade(pessoas)

print(maior)
print(media)
