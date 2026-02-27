def manipular_arquivo():
    with open("dados.txt", "w") as arquivo:
        for i in range(1,6):
            arquivo.write(f"linha {i}\n")

    with open("dados.txt", "r") as arquivo:
        conteudo = arquivo.read()
        print(conteudo)

manipular_arquivo()

def criar_relatorio():
    with open("relatorio.txt", "w") as relatorio:
        relatorio.write(f"RELATÓRIO DIÁRIO \n" "FATURAMENTO: 400\n" "COMBUSTÍVEL:100\n" "LUCRO:300\n" "META ATINGIDA\n")
    with open("relatorio.txt", "r") as relatorio:
        leitura_relatorio = relatorio.read()
        print(leitura_relatorio)

criar_relatorio()

def imprime_pessoas():
    pessoas = {
        "LUIS": 10,
        "ELYDA": 10,
        "GAEL": 10
    }

    with open("NOTAS.txt", "w") as relatorio_de_notas:
        for pessoa in pessoas.items():
            relatorio_de_notas.write(f"{pessoa}\n")
    with open("NOTAS.txt", "r") as relatorio_de_notas:
        ler_notas = relatorio_de_notas.read()
        print(ler_notas)


imprime_pessoas()
