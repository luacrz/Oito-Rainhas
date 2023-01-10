from rainhas_oito import Matriz
'''teste 1 - verificar se a entrada é válida'''

def teste_entrada():
    teste = Matriz([[0, 0, 0, 0, 2, 0, 0, 0], 
        [0, 1, 0, 0, 0, 0, 0, 0], 
        [0, 0, 0, 1, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 1, 0], 
        [0, 0, 1, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 0, 0, 0, 1], 
        [0, 0, 0, 0, 0, 1, 0, 0], 
        [1, 0, 0, 0, 0, 0, 0, 0]])
    
    assert teste.entrada_valida() == 0
    

