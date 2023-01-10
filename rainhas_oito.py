'''Tabuleiro'''
class Matriz:
    def __init__(self, matriz):
        self.tabuleiro = matriz

    def entrada_valida(self):
        soma = 0
        for linha in self.tabuleiro:
            soma = linha.count(1)
        if soma != 8:
            return -1
        if len(self.tabuleiro) != 8:
            return -1
        for linha in self.tabuleiro:
            if len(linha) != 8:
                return -1
            for posicao in linha:
                if posicao not in [0,1]:
                    return -1
        return 0

