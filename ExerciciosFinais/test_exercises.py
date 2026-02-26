from exercises import verifica_maior_numero, multiplicar, multiplo_de_cinco

def test_verifica_maior_numero():
    lista = [20,30,40,50,100]
    assert verifica_maior_numero(lista) == 100

def test_multiplicar():
    assert multiplicar(100, 200) == 20000
    assert multiplicar(1, 5) == 5
    

def test_multiplo_de_cinco():
    assert multiplo_de_cinco(45) == True
    assert multiplo_de_cinco(15) == True
    assert multiplo_de_cinco(1) == False
    
