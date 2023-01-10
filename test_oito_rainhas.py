from oito_rainhas import Matriz
'''teste 1 - verificar se a entrada é válida'''

def teste_entrada():
    teste = Matriz([[0, 0, 0, 0, 1, 0, 0, 0], 
                    [0, 1, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 1, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 1, 0], 
                    [0, 0, 1, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 1], 
                    [0, 0, 0, 0, 0, 1, 0, 0], 
                    [1, 0, 0, 0, 0, 0, 0, 0]])
    
    assert teste.entrada_valida() == 0


def teste_validar():
    teste = Matriz([[0, 0, 0, 0, 1, 0, 0, 0], 
                    [0, 1, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 1, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 1, 0], 
                    [0, 0, 1, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 1], 
                    [0, 0, 0, 0, 0, 1, 0, 0], 
                    [1, 0, 0, 0, 0, 0, 0, 0]])
    
    assert teste.solucao_valida() == 1

def teste_nao_e_solucao():
    teste = Matriz([[0, 0, 0, 0, 0, 1, 0, 0], 
                    [0, 1, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 1, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 1, 0], 
                    [0, 0, 1, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 1], 
                    [0, 0, 0, 0, 0, 1, 0, 0], 
                    [1, 0, 0, 0, 0, 0, 0, 0]])
    
    assert teste.solucao_valida() == 0

def teste_tabuleiro_invalido():
    teste = Matriz([[0, 0, 0, 0, 1, 0, 0, 0], 
                    [0, 1, 0, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 1, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 1, 0], 
                    [0, 0, 1, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 1], 
                    [0, 0, 0, 0, 0, 1, 0, 0], 
                    [1, 0, 0, 0, 0]])
    
    assert teste.solucao_valida() == -1

def teste_numeros_invalidos():
    teste = Matriz([[1, 2, 3, 4, 5, 6, 7, 8], 
                    [0, 1, 0, 0, 0, 0, 0, 0], 
                    [9, 1, 3, 1, 6, 0, 9, 0], 
                    [0, 0, 0, 0, 0, 0, 1, 0], 
                    [0, 0, 1, 0, 0, 0, 0, 0], 
                    [0, 0, 0, 0, 0, 0, 0, 1], 
                    [0, 0, 0, 0, 0, 1, 0, 0], 
                    [1, 0, 0, 0, 0]])
    
    assert teste.solucao_valida() == -1

