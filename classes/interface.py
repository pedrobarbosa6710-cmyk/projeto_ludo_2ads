#Importando a bibliotecas
import pygame

#Cria classe da interface
class Interface:
    def __init__(self, jogo, imagens, posicoes_imagens):
        self.jogo = jogo #Variavel que atribui o objeto do jogo
        self.imagens = imagens #Variável que atribui o dicionário de imagens
        self.posicao_imagens = posicoes_imagens #Variável que atribui o dicionário de posição das imagens
        
        #Dicionário que guarda se o botão é a versão normal (0) ou alternativa (1)
        self.botao_alternativo = {
            'botao_jogar': 0,
            'botao_creditos': 0,
            'botao_voltar_para_inicio': 0,
            'botao_confirmacao': 0,
            'botao_cancelar': 0,
        }

        #Variável que armazena as áreas clicaveis
        self.areas_clicaveis = {
            'icone_dado': self.cria_area_clicavel('imagens/icones', 'icon_dado'),
            'imagem_2ads': self.cria_area_clicavel('imagens/icones', 'icon_2ads'),
            'botao_jogar': self.cria_area_clicavel('imagens/icones', 'botao_jogar', self.botao_alternativo['botao_jogar']),
            'botao_creditos': self.cria_area_clicavel('imagens/icones', 'botao_creditos', self.botao_alternativo['botao_creditos']),
            'botao_voltar_para_inicio': self.cria_area_clicavel('imagens/icones', 'botao_voltar_para_inicio', self.botao_alternativo['botao_voltar_para_inicio']),
            'botao_confirmacao': self.cria_area_clicavel('imagens/icones', 'botao_confirmacao', self.botao_alternativo['botao_confirmacao']),
            'botao_cancelar': self.cria_area_clicavel('imagens/icones', 'botao_cancelar', self.botao_alternativo['botao_cancelar']),
            'botao_voltar': self.cria_area_clicavel('imagens/icones', 'botao_voltar'),
            'botao_sair': self.cria_area_clicavel('imagens/icones', 'botao_sair')
        }
       
    #Desenha os elementos da tela de inicio 
    def desenho_tela_inicio(self):
        self.jogo.tela.blit(self.imagens['fundo_alternativo'], (self.posicao_imagens['fundos'])) #Desenha o fundo da tela
        self.jogo.tela.blit(self.imagens['titulo_inicio'], (self.posicao_imagens['titulo_inicio'])) #Desenha o titulo do jogo
        self.jogo.tela.blit(self.imagens['botao_jogar'][self.botao_alternativo['botao_jogar']], (self.posicao_imagens['botao_jogar'])) #Desenha o botão de jogar
        self.jogo.tela.blit(self.imagens['botao_creditos'][self.botao_alternativo['botao_creditos']], (self.posicao_imagens['botao_creditos'])) #Desenha o botão de créditos
        self.jogo.tela.blit(self.imagens['icon_2ads'], (self.posicao_imagens['icon_2ads'])) #Desenha o icon de 2ads
        
     #Desenha os elementos da tela do jogo
    def desenho_tela_jogo(self):
        cor_borda = 0, 0, 0 #Indica que da borda é cor preta
        borda_largura = 700 #Indica a largura da borda
        borda_altura = 700 #Indica a altura da borda
        borda_x, borda_y = (self.jogo.tela_largura-borda_largura)/2, (self.jogo.tela_altura-borda_altura)/2 #Variável que guarda a fórmula da centralidade da borda
        borda = pygame.Rect(borda_x, borda_y, borda_largura, borda_altura) #Variável que guarda o retângulo da borda
        
        self.jogo.tela.blit(self.imagens['fundo_padrao'], (self.posicao_imagens['fundos']))
        self.jogo.tela.fill(cor_borda, borda) #Desenha a borda do tabuleiro
        self.jogo.tela.blit(self.imagens['tabuleiro'], (self.posicao_imagens['tabuleiro'])) #Desenha o fundo do tabuleiro
        self.jogo.tela.blit(self.imagens['icon_dado'], (self.posicao_imagens['icon_dado'])) #Desenha o icone do dado
        self.jogo.tela.blit(self.imagens['icon_turno'], (self.posicao_imagens['icon_turno'])) #Desenha o icone de turno
        self.jogo.tela.blit(self.imagens[self.jogo.identificacao_de_turno[self.jogo.turno_atual]][0], (self.posicao_imagens['icon_peca_turno'])) #Desenha a peça do turno atual
        self.jogo.tela.blit(self.imagens['botao_sair'], self.posicao_imagens['botao_sair'])
        self.jogo.tela.blit(self.imagens['icon_2ads'], (self.posicao_imagens['icon_2ads'])) #Desenha o icon de 2ads
       
        if self.jogo.dado_status == False:  #Caso o dado não possa ser jogado novamente
            self.jogo.tela.blit(self.imagens['icon_cadeado'], (self.posicao_imagens['icon_cadeado'])) #Coloca um simbolo de cadeado no dado
        
        if self.jogo.resultado_dado > 0: #Condição que verifica se o valor do dado já foi sorteado
            self.jogo.tela.blit(self.imagens['faces_dado'][self.jogo.resultado_dado], self.posicao_imagens['faces_dado']) #Caso sim, desenha a face correspondente ao resultado
                        
        #Loop que passa por todos os dados do peão
        for grupo in self.jogo.peoes.values():
            for peca in grupo.values():
                self.jogo.tela.blit(peca.imagens[peca.imagem_atual], self.jogo.coordenadas_peao(peca)) #Desenha o peão do loop
                            
        #Se o jogador quiser sair
        if self.jogo.tela_atual == 'jogo' and self.jogo.confirmacao_sair:
            self.desenho_confirmacao_sair() #Mostrar tela de confirmacao
            
     #Desenha os elementos da tela de confirmação
    def desenho_confirmacao_sair(self):
       self.jogo.tela.blit(self.imagens['fundo_escuro'], self.posicao_imagens['fundos']) #Desenha o fundo
       self.jogo.tela.blit(self.imagens['fundo_confirmacao'], self.posicao_imagens['fundo_confirmacao']) #Desenha o painel de confimação
       self.jogo.tela.blit(self.imagens['botao_confirmacao'][self.botao_alternativo['botao_confirmacao']], self.posicao_imagens['botao_confirmacao']) #Desenha o botão de confirmação
       self.jogo.tela.blit(self.imagens['botao_cancelar'][self.botao_alternativo['botao_cancelar']], self.posicao_imagens['botao_cancelar']) #Desenha o botão de cancelar
       
     #Desenha os elementos da tela de vitória
    def desenho_tela_vitoria(self):
        self.jogo.tela.blit(self.imagens['fundo_alternativo'], (self.posicao_imagens['fundos'])) #Desenha o fundo  
        if self.jogo.verificar_ganhador() is not None and self.jogo.jogo_encerrado is True: #Se o jogo já tiver um ganhador
            self.jogo.tela.blit(pygame.transform.scale(self.imagens[self.jogo.verificar_ganhador()][0], (320, 320)), (self.posicao_imagens['peca_vencedora'])) #Desenha a peça da cor vencedora
            self.jogo.tela.blit(self.imagens['vencedor'][self.jogo.verificar_ganhador()], (self.posicao_imagens['vencedor'])) #Desenha o texto que indica a cor vencedora
        self.jogo.tela.blit(self.imagens['botao_voltar_para_inicio'][self.botao_alternativo['botao_voltar_para_inicio']], (self.posicao_imagens['botao_voltar_para_inicio'])) #Desenha o botão para voltar ao inicio
        
     #Desenha os elementos da tela de créditos
    def desenho_tela_creditos(self):
        self.jogo.tela.blit(self.imagens['fundo_alternativo'], (self.posicao_imagens['fundos'])) #Desenha o fundo
        self.jogo.tela.blit(self.imagens['tela_de_creditos'], self.posicao_imagens['tela_de_creditos']) #Desenha a tela de créditos
        self.jogo.tela.blit(self.imagens['botao_voltar'], self.posicao_imagens['botao_voltar']) #Desenha o botão de voltar
            
    #Função que desenha as imagens fixas
    def desenho_imagens(self):
                
        #Desenha somente as imagens da tela de inicio
        if self.jogo.tela_atual == 'inicio':          
            self.desenho_tela_inicio()
                            
        elif self.jogo.tela_atual == 'jogo':     
            self.desenho_tela_jogo()
                    
        elif self.jogo.tela_atual == 'vitoria':
            self.desenho_tela_vitoria()
                    
        elif self.jogo.tela_atual == 'creditos':
            self.desenho_tela_creditos()

    #Método que cria a área clicável de um peão ou de uma imagem, conforme o tipo informado
    def cria_area_clicavel(self, objeto, elemento=None, alternativo=None):
        
        if self.jogo.tela_atual == 'inicio':
            if alternativo is None:  #Se for uma imagem que fica alternativa
                area_clicavel_imagem = self.imagens[elemento].get_rect() #Variável que armazena um retangulo clicavel com base no tamanho da imagem
            else: #Se for uma imagem normal
                area_clicavel_imagem = self.imagens[elemento][alternativo].get_rect() #Variável que armazena um retangulo clicavel com base no tamanho da imagem
            area_clicavel_imagem.topleft = self.posicao_imagens[elemento] #Define as coordenadas desse retangulo clicavel
            return area_clicavel_imagem #Retorna area clicável
        
        elif self.jogo.tela_atual == 'jogo':
            if objeto == 'peoes': #Se o objeto for um peão
                peao = elemento
                area_clicavel_peao = peao.imagens[peao.imagem_atual].get_rect() #Variável que armazena um retangulo clicavel com base no tamanho da imagem
                area_clicavel_peao.topleft = self.jogo.coordenadas_peao(peao) #Define as coordenadas desse retangulo clicavel
                return area_clicavel_peao #Retorna area clicável
            area_clicavel_imagem = self.imagens[elemento].get_rect() #Variável que armazena um retangulo clicavel com base no tamanho da imagem
            area_clicavel_imagem.topleft = self.posicao_imagens[elemento] #Define as coordenadas desse retangulo clicavel
            return area_clicavel_imagem #Retorna area clicável
        
        elif self.jogo.tela_atual == 'vitoria':
            if alternativo is None:  # Se for uma imagem única
                area_clicavel_imagem = self.imagens[elemento].get_rect()
            else:  # Se for uma lista de imagens alternativas
                area_clicavel_imagem = self.imagens[elemento][alternativo].get_rect()
            area_clicavel_imagem.topleft = self.posicao_imagens[elemento]
            return area_clicavel_imagem
        
        elif self.jogo.tela_atual == 'creditos':
            area_clicavel_imagem = self.imagens[elemento].get_rect() #Variável que armazena um retangulo clicavel com base no tamanho da imagem
            area_clicavel_imagem.topleft = self.posicao_imagens[elemento] #Define as coordenadas desse retangulo clicavel
            return area_clicavel_imagem #Retorna area clicável

    #Método que verifica se o mouse está sobre uma área clicável é qual o tipo de ação do mouse sobre ele
    def sobre_area_clicavel(self, tipo, posicao_mouse, objeto=None, peca=None, elemento=None):
        
        if self.jogo.tela_atual == 'inicio':
            if tipo == 'mouse_passando_por_cima': #Caso o mouse passe por cima
                self.botao_alternativo['botao_jogar'] = int(self.areas_clicaveis['botao_jogar'].collidepoint(posicao_mouse)) #retorna 0 ou 1
                self.botao_alternativo['botao_creditos'] = int(self.areas_clicaveis['botao_creditos'].collidepoint(posicao_mouse)) #retorna 0 ou 1
                #Variável que armazena um valor de verdadeiro ou falso, dependendo se o mouse passou por cima ou não
                cursor_interativo = (
                    self.areas_clicaveis['imagem_2ads'].collidepoint(posicao_mouse) or
                    self.areas_clicaveis['botao_jogar'].collidepoint(posicao_mouse) or 
                    self.areas_clicaveis['botao_creditos'].collidepoint(posicao_mouse)
                )
                if cursor_interativo: #Se Verdadeiro muda o cursor para uma mão
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else: #Se Falso muda o cursor para uma seta
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  
            elif tipo == 'mouse_clicou_em_cima': #Caso o mouse clique em cima
                if objeto == 'imagens/icones': #Caso for em uma imagem ou icone
                    return self.areas_clicaveis[elemento].collidepoint(posicao_mouse) #Retorna verdadeiro ou Falso       
                    
        elif self.jogo.tela_atual == 'jogo':
            if tipo == 'mouse_passando_por_cima': #Caso o mouse passe por cima
                self.botao_alternativo['botao_confirmacao'] = int(self.areas_clicaveis['botao_confirmacao'].collidepoint(posicao_mouse)) #retorna 0 ou 1
                self.botao_alternativo['botao_cancelar'] = int(self.areas_clicaveis['botao_cancelar'].collidepoint(posicao_mouse)) #retorna 0 ou 1
                #Variável que armazena um valor de verdadeiro ou falso, dependendo se o mouse passou por cima ou não

                cursor_interativo = False #Indica que o cursor não é interativo

                cursor_interativo = (
                    (self.jogo.dado_status and self.areas_clicaveis['icone_dado'].collidepoint(posicao_mouse)) or
                    self.areas_clicaveis['imagem_2ads'].collidepoint(posicao_mouse) or
                    self.areas_clicaveis['botao_sair'].collidepoint(posicao_mouse) 
                )
                #Procura entre os peões
                for grupo in self.jogo.peoes.values():
                    for peca in grupo.values():
                        if (self.cria_area_clicavel('peoes', peca).collidepoint(posicao_mouse) and self.jogo.movimento_valido(peca)):
                            cursor_interativo = True #Retorna Verdadeiro

                #Verifica se os botões de cancelamento e confirmamento podem ser clicados
                if self.jogo.confirmacao_sair:
                    if (
                        self.areas_clicaveis['botao_confirmacao'].collidepoint(posicao_mouse) or
                        self.areas_clicaveis['botao_cancelar'].collidepoint(posicao_mouse)
                    ):
                        cursor_interativo = True

                if cursor_interativo: #Se Verdadeiro muda o cursor para uma mão
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else: #Se Falso muda o cursor para uma seta
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)

            elif tipo == 'mouse_clicou_em_cima': #Caso o mouse clique em cima
                if objeto == 'peoes': #Caso for em um peão
                    return self.cria_area_clicavel('peoes', peca).collidepoint(posicao_mouse) #Retorna verdadeiro ou Falso
                elif objeto == 'imagens/icones': #Caso for em uma imagem ou icone
                    return self.areas_clicaveis[elemento].collidepoint(posicao_mouse) #Retorna verdadeiro ou Falso
                
        elif self.jogo.tela_atual == 'vitoria':
            if tipo == 'mouse_passando_por_cima': #Caso o mouse passe por cima
                self.botao_alternativo['botao_voltar_para_inicio'] = int(self.areas_clicaveis['botao_voltar_para_inicio'].collidepoint(posicao_mouse)) #retorna 0 ou 1
                #Variável que armazena um valor de verdadeiro ou falso, dependendo se o mouse passou por cima ou não
                cursor_interativo = (
                    self.areas_clicaveis['botao_voltar_para_inicio'].collidepoint(posicao_mouse)
                )
                if cursor_interativo: #Se Verdadeiro muda o cursor para uma mão
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else: #Se Falso muda o cursor para uma seta
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
            elif tipo == 'mouse_clicou_em_cima': #Caso o mouse clique em cima
                if objeto == 'imagens/icones': #Caso for em uma imagem ou icone
                    return self.areas_clicaveis[elemento].collidepoint(posicao_mouse) #Retorna verdadeiro ou Falso
        
        elif self.jogo.tela_atual == 'creditos':
            if tipo == 'mouse_passando_por_cima': #Caso o mouse passe por cima
                #Variável que armazena um valor de verdadeiro ou falso, dependendo se o mouse passou por cima ou não
                cursor_interativo = (
                    self.areas_clicaveis['botao_voltar'].collidepoint(posicao_mouse) 
                )
                if cursor_interativo: #Se Verdadeiro muda o cursor para uma mão
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
                else: #Se Falso muda o cursor para uma seta
                    pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW) 
            elif tipo == 'mouse_clicou_em_cima': #Caso o mouse clique em cima
                    return self.areas_clicaveis[elemento].collidepoint(posicao_mouse) #Retorna verdadeiro ou Falso
                

