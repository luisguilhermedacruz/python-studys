## -*- coding: utf-8 -*-

arquivo = open("arquivo.txt")

linhas = arquivo.read()

print(linhas) 

w = open("arquivo.txt", "a")
w.write("Esse é o meu arquivo de teste 2\n")
w.close()