#Importando a bibliotecas
import pygame

#Cria classe da interface
class Interface:
    def __init__(self, jogo, imagens, posicoes_imagens):
        self.jogo = jogo #Variavel que atribui o objeto do jogo
        self.imagens = imagens #Variável que atribui o dicionário de imagens
        self.posicao_imagens = posicoes_imagens #Variável que atribui o dicionário de posição das imagens

        #Variável que armazena as áreas clicaveis
        self.areas_clicaveis = {
            'icone_dado': self.cria_area_clicavel('imagens/icones', 'icon_dado'),
            'imagem_2ads': self.cria_area_clicavel('imagens/icones', 'icon_2ads')
        }

    #Função que desenha as imagens fixas
    def desenho_imagens(self):

        cor_do_fundo = 0, 200, 0 #Cor do fundo da tela (verde)

        cor_borda = 0, 0, 0 #Indica que da borda é cor preta
        borda_largura = 700 #Indica a largura da tela
        borda_altura = 700 #Indica a altura da tela
        borda_x, borda_y = (900-borda_largura)/2, (760-borda_altura)/2 #Variável que guarda a fórmula da centralidade da borda
        borda = pygame.Rect(borda_x, borda_y, borda_largura, borda_altura) #Variável que guarda o retângulo da borda

        self.jogo.tela.fill((cor_do_fundo)) #Desenha o fundo da tela
        self.jogo.tela.fill(cor_borda, borda) #Desenha a borda do tabuleiro
        self.jogo.tela.blit(self.imagens['tabuleiro'], (self.posicao_imagens['tabuleiro'])) #Desenha o fundo do tabuleiro
        self.jogo.tela.blit(self.imagens['icon_dado'], (self.posicao_imagens['icon_dado'])) #Desenha o icone do dado
        self.jogo.tela.blit(self.imagens['icon_2ads'], (self.posicao_imagens['icon_2ads'])) #Desenha o icon de 2ads

        if self.jogo.resultado_dado > 0: #Condição que verifica se o valor do dado já foi sorteado
            self.jogo.tela.blit(self.imagens['faces_dado'][self.jogo.resultado_dado], self.posicao_imagens['faces_dado']) #Caso sim, desenha a face correspondente ao resultado

        #Loop que passa por todos os dados do peão
        for grupo in self.jogo.peoes.values():
            for peca in grupo.values():
                self.jogo.tela.blit(peca.imagens[peca.imagem_atual], self.jogo.coordenadas_peao(peca)) #Desenha o peão do loop

    #Método que cria a área clicável de um peão ou de uma imagem, conforme o tipo informado
    def cria_area_clicavel(self, objeto, elemento=None):
        if objeto == 'peoes':
            peao = elemento
            area_clicavel_peao = peao.imagens[peao.imagem_atual].get_rect() #Variável que armazena um retangulo clicavel com base no tamanho da imagem
            area_clicavel_peao.topleft = self.jogo.coordenadas_peao(peao) #Define as coordenadas desse retangulo clicavel
            return area_clicavel_peao #Retorna area clicável

        area_clicavel_imagem = self.imagens[elemento].get_rect() #Variável que armazena um retangulo clicavel com base no tamanho da imagem
        area_clicavel_imagem.topleft = self.posicao_imagens[elemento] #Define as coordenadas desse retangulo clicavel
        return area_clicavel_imagem #Retorna area clicável

    #Método que verifica se o mouse está sobre uma área clicável é qual o tipo de ação do mouse sobre ele
    def sobre_area_clicavel(self, tipo, posicao_mouse, objeto=None, peca=None, elemento=None):

        if tipo == 'mouse_passando_por_cima': #Caso o mouse passe por cima

            #Variável que armazena um valor de verdadeiro ou falso, dependendo se o mouse passou por cima ou não
            cursor_interativo = (
                self.areas_clicaveis['imagem_2ads'].collidepoint(posicao_mouse)
                or (self.jogo.dado_status and self.areas_clicaveis['icone_dado'].collidepoint(posicao_mouse))
            )

            #Procura entre os peões
            for grupo in self.jogo.peoes.values():
                for peca in grupo.values():
                    if (self.cria_area_clicavel('peoes', peca).collidepoint(posicao_mouse) and self.jogo.movimento_valido(peca)):
                        cursor_interativo = True #Retorna Verdadeiro

            if cursor_interativo: #Se Verdadeiro muda o cursor para uma mão
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else: #Se Falso muda o cursor para uma seta
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

        elif tipo == 'Mouse_clicou_em_cima': #Caso o mouse clique em cima

            if objeto == 'peoes': #Caso for em um peão
                return self.cria_area_clicavel('peoes', peca).collidepoint(posicao_mouse) #Retorna verdadeiro ou Falso
            elif objeto == 'imagens/icones': #Caso for em uma imagem ou icone
                return self.areas_clicaveis[elemento].collidepoint(posicao_mouse) #Retorna verdadeiro ou Falso