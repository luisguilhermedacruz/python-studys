## -*- coding: utf-8 --*--

##teste1

numero1 = 10
numero2 = 20

if numero1 > numero2:
    print("O número 1 é maior que o número 2")
elif numero1 < numero2:
    print("O numero 1 é menor que o numero 2")
else:
    print("Os numeros são iguais!")        


#teste2

a = 5
b = 5.0
c = "5"

print("Letra a tem um valor de ",a, " e é do tipo ", (type(a)))
print("Letra a tem um valor de ",b, " e é do tipo ", (type(b)))
print("Letra a tem um valor de ",c, " e é do tipo ", (type(c)))
print(a == b)
print(a == c)
print(b == c)

#teste3 

nome = "Luis"
idade = 25

print("Meu nome é: ", nome, "e eu tenho ", str(idade), " anos")


#teste4

nota = 5
media = 7
notaDeRecuperacao = media - nota
aluno = "Luis Guilherme"

if nota >= 7:
    print(aluno.upper(), "ESTÁ APROVADO!")
elif nota <= 5:
    print(aluno.upper(), "ESTÁ EM RECUPERAÇÃO PRECISANDO DE: ", notaDeRecuperacao )
else:
    print(aluno.upper(), "ESTÁ REPROVADO!")        

#teste5

tem_carteira = True
idade = 18

if tem_carteira == True and idade >= 18:
    print("Pode dirigir!")
else:
    print("Não pode dirigir!")