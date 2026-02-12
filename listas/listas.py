## --*-- coding: utf-8 --*--

minha_lista = ["abacaxi", "melancia", "abacate"]
minha_lista2 = [1,2,3,4,5]
minha_lista3 = ["abacaxi", 2, 9.89, True]

frutas = minha_lista

for itemsDeFrutas in frutas:
    print(itemsDeFrutas)

tamanho = len(frutas)
print(tamanho)

frutas.append("maça")
print(frutas)
 
if "banana" in frutas:
    print("Existe um abacaxi na sua cesta!")


del frutas[1:3]
print(frutas)