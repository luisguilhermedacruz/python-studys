lista = [1,2,3,4,5]

def verifica_maior_numero(lista: list[int]) -> int:
        maior_numero = lista[0]
        for n in lista[1:]:
                if n > maior_numero:
                    maior_numero = n
        return maior_numero



def multiplicar(a: int, b: int) -> int:
       return a * b

def multiplo_de_cinco(numero: int) -> bool:
       if numero % 5 == 0:
              return True
       else:
              return False
    
print(verifica_maior_numero(lista))
print(multiplicar(10,30))
print(multiplo_de_cinco(45))

