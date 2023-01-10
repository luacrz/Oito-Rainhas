'''O objetivo da classe é verificar se a entrada (o tabuleiro)
    contém a solução para o problema das 8 rainhas'''
class Matriz:
    def __init__(self, matriz):
        self.tabuleiro = matriz

    def entrada_valida(self):
        '''Função para verificar se a entrada é válida'''
        soma = 0
        for linha in self.tabuleiro:
            soma += linha.count(1)
        if soma != 8:
            return -1
        if len(self.tabuleiro) != 8:
            return -1
        for linha in self.tabuleiro:
            if len(linha) != 8:
                return -1
            for posicao in linha:
                if posicao not in [0, 1]:
                    return -1
        return 0

    def solucao_valida(self):
        '''Função para validar a entrada'''
        if self.entrada_valida() == -1:
            return -1
        for indice2 in range(len(self.tabuleiro)):
            soma = 0
            for indice1 in range(len(self.tabuleiro)):
                soma += self.tabuleiro[indice1][indice2]
            if soma > 1:
                return 0
        for indice1 in range(len(self.tabuleiro)):
            soma = 0
            for indice2 in range(len(self.tabuleiro)):
                soma += self.tabuleiro[indice1][indice2]
            if soma > 1:
                return 0
        for primeiro_lado in range(len(self.tabuleiro)-2, 0, -1):
            soma = 0
            for indice in range(len(self.tabuleiro)):
                soma += self.tabuleiro[primeiro_lado+indice][indice]
                if primeiro_lado+indice == 7:
                    break
            if soma > 1:
                return 0
        if sum(self.tabuleiro[meio][meio] for meio in range(len(self.tabuleiro))) > 1:
            return 0
        for central in range(1, len(self.tabuleiro)-1):
            soma = 0
            for indice in range(len(self.tabuleiro)):
                soma += self.tabuleiro[indice][central+indice]
                if central+indice == len(self.tabuleiro)-1:
                    break
            if soma > 1:
                return 0
        for central in range(1, len(self.tabuleiro)-1):
            soma = 0
            for indice in range(len(self.tabuleiro)):
                soma += self.tabuleiro[indice][central-indice]
                if central-indice == 0 or indice == len(self.tabuleiro)-1:
                    break
            if soma > 1:
                return 0
        if sum(self.tabuleiro[begin][end]
                for begin, end in
                zip(range(len(self.tabuleiro)), range(len(self.tabuleiro)-1, -1, -1))) > 1:
            return 0
        for segundo_lado in range(1, len(self.tabuleiro)-1):
            soma = 0
            for indice in range(len(self.tabuleiro)):
                soma += self.tabuleiro[segundo_lado+indice][7-indice]
                if segundo_lado+indice == len(self.tabuleiro)-1:
                    break
            if soma > 1:
                return 0
        return 1
