idade = int(input("Qual sua idade?"))
nome = input("Qual sua seu nome?")

if idade >= 18:
    print(f"O {nome} tem {idade} anos e é maior de idade!")
else:
    print(f"O {nome} tem {idade} e ainda é menor de idade!")


nota1 = float(input("Qual sua primeira nota?"))
nota2 = float(input("Qual sua segunda nota?"))


maior_nota = max(nota1, nota2)



if nota1 >= 6 or nota2 >= 6:
    print(f"O aluno atingiu a aprovação com a nota {maior_nota}")
else:
    print(f"Aluno foi reprovado pois nenhuma das notas atingiu o minimo.")

def calculadora(x,y,z):
    return (x*y)+z

print(calculadora(10,2,3))