classificadosOitavas = [
    {"posição": 1, "nome": "Novo Horizontino", "pontos": 16},
    {"posição": 2, "nome": "Palmeiras", "pontos": 16},
    {"posição": 3, "nome": "Bragantino", "pontos": 16},
    {"posição": 4, "nome": "Portuguesa", "pontos": 15},
    {"posição": 5, "nome": "Corinthians", "pontos": 14},
    {"posição": 6, "nome": "São Paulo", "pontos": 13},
    {"posição": 7, "nome": "Capivariano", "pontos": 13},
    {"posição": 8, "nome": "Santos", "pontos": 12},
]

classificadoQuartas = []
relatorio = []

for i in range(4):

    timeA = classificadosOitavas[i]
    timeB = classificadosOitavas[7 - i]

    print("\nConfronto:")
    print(timeA["nome"], "x", timeB["nome"])

    golsA = int(input("Gols do " + timeA["nome"] + ": "))
    golsB = int(input("Gols do " + timeB["nome"] + ": "))

    
    if golsA > golsB:
        print(timeA["nome"], "venceu no tempo normal!")
        timeA["pontos"] += 3
        classificadoQuartas.append(timeA)
        relatorio.append(f"{timeA['nome']} {golsA} x {golsB} {timeB['nome']} - Vitória no tempo normal")

    elif golsB > golsA:
        print(timeB["nome"], "venceu no tempo normal!")
        timeB["pontos"] += 3
        classificadoQuartas.append(timeB)
    
    else:
        print("Empate! Vamos para os pênaltis.")

        penA = int(input("Gols nos pênaltis do " + timeA["nome"] + ": "))
        penB = int(input("Gols nos pênaltis do " + timeB["nome"] + ": "))

        if penA > penB:
            print(timeA["nome"], "venceu nos pênaltis!")
            timeA["pontos"] += 1
            classificadoQuartas.append(timeA)
            relatorio.append(f"{timeA['nome']} {golsA} x {golsB} {timeB['nome']} - Decidido nos pênaltis")
        else:
            print(timeB["nome"], "venceu nos pênaltis!")
            timeB["pontos"] += 1
            classificadoQuartas.append(timeB)
            relatorio.append(f"{timeA['nome']} {golsA} x {golsB} {timeB['nome']} - Decidido nos pênaltis")


classificadoQuartas.sort(key=lambda time: time["pontos"], reverse=True)


print("\nClassificados para próxima fase:")
for time in classificadoQuartas:
    print(time["nome"], "-", time["pontos"], "pontos")


with open("relatorio.txt", "w", encoding="utf-8") as arquivo:

    arquivo.write("===== CONFRONTOS =====\n\n")

    for linha in relatorio:
        arquivo.write(linha + "\n")

    arquivo.write("\n===== CLASSIFICAÇÃO =====\n\n")

    for i, time in enumerate(classificadoQuartas, start=1):
        arquivo.write(f"{i}º - {time['nome']} ({time['pontos']} pontos)\n")





