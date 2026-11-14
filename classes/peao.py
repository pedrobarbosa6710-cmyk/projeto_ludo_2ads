#Classe que define as caracteristicas dos Peões
class Peao:
    def __init__(self, cor, numero, imagens):
        self.cor = cor #Variavel que guarda a cor do peão
        self.numero = numero #Variavel que guarda a numeração do peão , vai de 1-4)
        self.posicao = None #Posição do peão. None = base, 1-36 = percurso, 37-40 = casas especiais
        self.imagens = imagens #Variavel que guarda o conjunto de imagens do peão
        self.imagem_atual = 0 #Variavel que guarda o indice para indicação de imagem