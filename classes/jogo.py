#Importando a bibliotecas
import pygame
import webbrowser
from random import shuffle, randint

from classes.peao import Peao #Importa a classe Peão

#Evento utilizado quando uma música termina
evento_fim_musica = pygame.USEREVENT + 1

#Classe que define as caracteristicas do Jogo
class Jogo:
    def __init__(self, tela_dimensoes, titulo, diretorio, casas_do_tabuleiro):
        self.jogo_ativo = True #Variavel que indica se o jogo está ativo ou desativo
        self.jogo_encerrado = False #Variavel que indica se o jogo acabou ou se ainda está em andamento
        
        self.casas_de_entrada = {'vermelho': 1, 'amarelo': 10, 'verde': 28,'azul': 19} #Dicionario das casas e coordenadas do tabuleiro
        self.casas_do_tabuleiro = casas_do_tabuleiro #Dicionario com as coordenadas do tabuleiro

        self.turno_atual = 0 #Idenficação do turno atual
        self.identificacao_de_turno = {0: 'vermelho', 1: 'amarelo', 2: 'azul', 3: 'verde'} #Dicionario para a identificação dos turnos dos jogadores
        self.dado_status = True #Variavel que indica se o dado pode ou não ser lançado
        self.resultado_dado = 0 #Variavel que guarda o valor gerado pelo dado. Caso 0, ainda não houve nenhum lançamento
        
        #Lista de Playlist
        self.musicas = [
            diretorio / 'assets' / 'sounds' / 'faixa_1.mp3',
            diretorio / 'assets' / 'sounds' / 'faixa_2.mp3',
            diretorio / 'assets' / 'sounds' / 'faixa_3.mp3',
            diretorio / 'assets' / 'sounds' / 'faixa_4.mp3',
            diretorio / 'assets' / 'sounds' / 'faixa_5.mp3',
            diretorio / 'assets' / 'sounds' / 'faixa_6.mp3',
            diretorio / 'assets' / 'sounds' / 'faixa_7.mp3',
            diretorio / 'assets' / 'sounds' / 'faixa_8.mp3',
            diretorio / 'assets' / 'sounds' / 'faixa_9.mp3',
            diretorio / 'assets' / 'sounds' / 'faixa_10.mp3'
        ]
        
        #Embaralhamento das músicas
        shuffle(self.musicas)

        #Loop da playlist
        self.musica_indice = 0
        pygame.mixer.music.set_endevent(evento_fim_musica)

        #Exercução das músicas
        pygame.mixer.music.load(str(self.musicas[self.musica_indice]))
        pygame.mixer.music.play()
                
        self.relogio = pygame.time.Clock() #Variavel que 
        self.tela_dimensoes = tela_dimensoes #Variavel que guarda as dimensões da tela
        self.tela = pygame.display.set_mode((self.tela_dimensoes)) #Variavel que armazena a tela
        
        pygame.display.set_caption(titulo) #Variavel que armazena o titulo da tela
        self.icon = None #Variavel que guarda o favicon da tela
        
    #Método que cria o dicionário dos peões
    def criar_peoes(self, imagens): 
        #Dicionário que armazena os objetos de peão que são utilizados no jogo       
        self.peoes = {
            'vermelho': {
                0: Peao('vermelho', 1, imagens['vermelho']),
                1: Peao('vermelho', 2, imagens['vermelho']),
                2: Peao('vermelho', 3, imagens['vermelho']),
                3: Peao('vermelho', 4, imagens['vermelho'])
            },
                    
            'amarelo': {
                0: Peao('amarelo', 1, imagens['amarelo']),
                1: Peao('amarelo', 2, imagens['amarelo']),
                2: Peao('amarelo', 3, imagens['amarelo']),
                3: Peao('amarelo', 4, imagens['amarelo'])
            },
                    
            'verde': {
                0: Peao('verde', 1, imagens['verde']),
                1: Peao('verde', 2, imagens['verde']),
                2: Peao('verde', 3, imagens['verde']),
                3: Peao('verde', 4, imagens['verde'])
            },  
            
            'azul': {
                0: Peao('azul', 1, imagens['azul']),
                1: Peao('azul', 2, imagens['azul']),
                2: Peao('azul', 3, imagens['azul']),
                3: Peao('azul', 4, imagens['azul'])
            }
        }
        
    #Método que processa os eventos do jogo
    def processar_eventos(self, eventos, interface):
        
        for event in eventos: #Percorre todos os eventos 
            
            if event.type == pygame.QUIT: #Se o evento for o fechamento do jogo
                self.jogo_ativo = False #Decalra que o jogo esta inativo, acabando como while
                
            elif event.type == pygame.MOUSEMOTION: #Se o evento for a movimentação do mouse
                interface.sobre_area_clicavel('mouse_passando_por_cima', event.pos) #Chama o método que verifica se é necessário a troca do ponteiro
                
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: #Se ocorrer um clique com o botão direito
                if not self.jogo_encerrado: #Se o jogo não tiver um ganhador
                    self.processar_clique(event.pos, interface) #Chama método que processa o clique
                    
            elif event.type == evento_fim_musica: #Se a música acabar
                self.atualizar_musicas() #Chama o método que atualiza a música
    
    #Método que processa os cliques realizado em peões        
    def processar_clique_peao(self, posicao_mouse, interface):
        #Decalara que nenhum movimento foi realizado 
        movimento_realizado = False
                        
        #Percorre os peões
        for grupo in self.peoes.values():
            for peca in grupo.values():
                                
                if interface.sobre_area_clicavel('Mouse_clicou_em_cima', posicao_mouse, objeto='peoes', peca=peca): #Verifica se ocorreu um clique sobre um peão
                                    
                    if self.movimento_valido(peca): #Verifica se a peça clicada pode exercer movimento, se Verdadeiro verifica as condições abaixo:
                                        
                        if peca.posicao is None: #caso a peça esteja na base, entra na primeira casa do seu percurso
                                    
                            self.executar_movimento('movimento_saida_da_base', peca) #Chama o método que executa o movimento para saida da base
                                            
                            if self.captura_valida_peca_saindo_da_base(peca) is True: #Na sua saída da base verifica se pode capturar uma peça adversária que está na sua casa segura, Se verdadeiro verifica as condições abaixo: 
                                self.executar_captura('captura_saindo_da_base', peca) #Chama o método qeu executa a captura da peça no caso da saida de base
                                                                
                        elif peca.posicao <= 36:  #Caso a peça esteja no trajeto, movimenta a peça
                                            
                            if self.captura_valida(peca): #Condição que verifica se a movimentação do peão podera capturar um peão adversario, Se verdadeiro verifica as condições abaixo: 
                                self.executar_captura('captura_no_percuso_principal', peca) #Chama o método qeu executa a captura da peça no caso do percurso
                                                                
                            #Ao final movimenta a peça com o resultado do dado   
                            self.executar_movimento('movimento_no_percurso_principal', peca) #Chama o método que executa o movimento para o percurso
            
                        else: #Caso ele esteja em um casa especial e o movimento for possível:
                            self.executar_movimento('movimento_nas_casas_especiais', peca) #Chama o método que executa o movimento para as casas especiais
                                        
                        if self.verificar_ganhador() is not None: #Condição que verifica se há um ganhador
                            self.fim_da_partida()#Executa o fim da partida
                                    
                        else: #Caso não, o jogo flui normalmente                              
                            self.controle_de_turno('troca_de_turno_pós_jogada', peca) #Executa o controle de turno
                                    
                        movimento_realizado = True #Declara que um movimento foi realizado    
                        break #Fecha os loops
                        
            if movimento_realizado: #Se o movimento já tiver sido realizado
                break #Fecha os loops
    
    #Método que processa os cliques realizado no icone do dado     
    def processar_clique_icone_dado(self, posicao_mouse, interface):
        if self.dado_status and interface.sobre_area_clicavel('Mouse_clicou_em_cima', posicao_mouse, objeto='imagens/icones', elemento='icone_dado'): #Caso clique em cima icone do dado
                    
            self.girar_dado() #Executa o giro do dado
            
            if not self.movimento_disponivel():  #Se não tiver nenhuma peça fora da base, muda o turno para o próximo jogador
                self.controle_de_turno('troca_de_turno_por_movimento_indisponivel') #Executa o controle de turno
    
    #Método que processa os cliques realizado na imagem do 2ads    
    def processar_clique_imagem_2ads(self, posicao_mouse, interface):
        if interface.sobre_area_clicavel('Mouse_clicou_em_cima', posicao_mouse, objeto='imagens/icones', elemento='imagem_2ads'): #Caso clique em cima do icon 2ads
            webbrowser.open("https://www.instagram.com/2adsistemas/") #Leva para o instagram da sala    
            
    #Método que processa chama os métodos de processo de clique
    def processar_clique(self, posicao_mouse, interface):
        self.processar_clique_peao(posicao_mouse, interface)
        self.processar_clique_icone_dado(posicao_mouse, interface)
        self.processar_clique_imagem_2ads(posicao_mouse, interface)
          
    #Método que gira o dado   
    def girar_dado(self):
        self.resultado_dado = randint(1,6) #Sorteia o número de 1-6
        self.dado_status = False #Bloqueia o dado
                
        #Guias do terminal
        print(' ')
        print(f'Resultado do dado foi: {self.resultado_dado}')
        print(f'Dado bloqueado')     
             
    #Método que relaciona a posição lógica da peça com a coordenada dela, retorna as coordenadas correspondentes
    def coordenadas_peao(self, peao):
            
        if peao.posicao is None: #Caso esteja na base
            return self.casas_do_tabuleiro[f'base_{peao.cor}'][peao.numero] #Retorna as coordenadas da base do peão correspondente
        
        elif peao.posicao <= 36: #Caso esteja no percurso

            casa_real = ((self.casas_de_entrada[peao.cor] + peao.posicao - 2) % 36) + 1 #Calcula as coordenadas reais do peão 
            return self.casas_do_tabuleiro[casa_real] #Retorna coordenadas do peão correspondente
        
        elif peao.posicao <= 40: #Caso esteja na reta final
            return self.casas_do_tabuleiro[f'final_{peao.cor}'][peao.posicao - 36] #Retorna as coordenadas da casa final correspondente
        
    #Método que verifica se há possibilidade de uma peça ser movida, retorna "True" ou "False"
    def movimento_valido(self, peao):
            
        if self.dado_status or self.identificacao_de_turno[self.turno_atual] != peao.cor: #Caso o jogador ainda não tenha girado o dado e não for o seu turno
            return False #Retorna Falso
        
        if peao.posicao is None:  #Caso a peça em que o jogador clicou ainda estiver na base, verifica se o resultado é igual a 6 ou 1
            return self.resultado_dado == 6 or self.resultado_dado == 1 #Retorna Verdadeiro ou Falso a depender do resultado do dado
        
        elif peao.posicao <= 36: #Caso a peça em que o jogador clicou estiver no percurso
            nova_posicao = peao.posicao + self.resultado_dado #Calcula a nova posição que a peça estará 

            if nova_posicao <= 36: #Verifca se a sua possível nova posição ainda está no percurso
                return True #Retorna Verdeiro
            
            return nova_posicao == 37 #Retorna um valor de Verdadeiro ou Falso dependendo da nova posição do peão

        
        elif peao.posicao < 40: #Caso a peça em que o jogador clicou esteja na reta final, compara se a casa especial corresponde ao resultado tirado, válida ou inválida a movimentação
            proxima_casa = peao.posicao - 35 #Variável que guarda o valor correspondete a sua casa final
            return self.resultado_dado == proxima_casa #Retorna um valor de Verdadeiro ou Falso
        
        return False #Retorna Falso
    
    #Método que verifica se há algum movimento disponível
    def movimento_disponivel(self):
        
        #Variável que indica a cor do turno atual
        cor_atual = self.identificacao_de_turno[self.turno_atual]
        
        #Procura entre todos os peões se tem algum que pode se movimentar
        movimento_disponivel = any(                                
            self.movimento_valido(peca)
            for peca in self.peoes[cor_atual].values()
        )
        
        return movimento_disponivel #Retorna Verdadeiro ou Falso
    
    #Método que executa o movimento
    def executar_movimento(self, tipo, peca):
        
        if tipo == 'movimento_saida_da_base': #caso a peça esteja na base
            peca.posicao = 1 #Posiciona ela na sua casa segura
        
        elif tipo == 'movimento_no_percurso_principal': #Caso a peça esteja no percurso
            peca.posicao += self.resultado_dado #Adiciona o resultado do dado a sua posição
        
        elif tipo == 'movimento_nas_casas_especiais': #Caso esteja nas casas especiais
            peca.posicao += 1 #Avança para a próxima casa espécial

    #Método que verifica se a futura movimentação de uma peça pode resultar em uma captura
    def captura_valida(self, peao):
        
        if peao.posicao + self.resultado_dado > 36: #Condição que verifica se a futura posição do peão está dentro da reta final
            return False #Retorna Falso
        
        futura_posicao = ((self.casas_de_entrada[peao.cor] + (peao.posicao + self.resultado_dado) - 2) % 36) + 1 #Variável que armazena o valor do calculo de onde ela estará ao realizar a movimentação
        
        #Procura entre os peões           
        for cor, grupo in self.peoes.items():
                for peca in grupo.values():
                    
                    if peca.posicao is not None and peca.posicao <= 36: #Se ele estiver no percurso principal
                        casa_progresso_em_curso = ((self.casas_de_entrada[cor] + peca.posicao - 2) % 36) + 1 #Calcula as coordenadas reais do peão
                        
                        if futura_posicao == casa_progresso_em_curso and peao.cor != peca.cor: #Se ele estiver dentro da casa segura não é capturável
                            if peca.posicao == 1: #Se a peça estiver na casa segura, ignora.
                                continue
                            else:
                                return True #Se ela puder se capturada retorna True
                                        
        return False #Se não encontrar peças capturaveis retorna False


    #Método que verifica se uma peça ao sair da base e ir para a casa segura pode eliminar uma peça adversária na mesma
    def captura_valida_peca_saindo_da_base(self, peao):

        #Procura entre os peões
        for cor, grupo in self.peoes.items():
            for peca in grupo.values():

                if peca.posicao is not None and peca.posicao <= 36: #Se ele estiver no percurso principal
                    casa_progresso_em_curso = ((self.casas_de_entrada[cor] + peca.posicao - 2) % 36) + 1 #Calcula as coordenadas reais do peão

                    if casa_progresso_em_curso == self.casas_de_entrada[peao.cor] and peao.cor != peca.cor: #Se a peça adversária estiver na base segura no momento da saida da peça da base correspondente é capturada
                        return True #Retorna Verdadeiro caso haja uma peça capturável
                
        return False #Retorna Falso caso não haja nenhuma peça capturável

    #Método que executa a captura da peça, na situação de saida da base (0) e no percurso (1)
    def executar_captura(self, tipo, peca):

        casa_futuro_progresso = ((self.casas_de_entrada[peca.cor] + (peca.posicao + self.resultado_dado) - 2) % 36) + 1 #Calcula a futura posição da peça
        
        #Percorre os peões
        for cores, grupos in self.peoes.items():
            for peao in grupos.values():         
                if peao.posicao is not None and peao.posicao <= 36: #Se o peão estiver no percurso principal
            
                    casa_progresso_em_curso = ((self.casas_de_entrada[cores] + peao.posicao - 2) % 36) + 1 #Calcula a posição do peão do loop
                    
                    if tipo == 'captura_saindo_da_base': #Se for no caso da saida da base
                        if casa_progresso_em_curso == self.casas_de_entrada[peca.cor] and peca.cor != peao.cor: #Se a casa da peça adversária em curso estiver na casa segura no momento em que o jogador sai da base
                            peao.posicao = None #Retorna o peão que estava na casa segura para a sua base, capturando a peça
                            print(f'Peça ({peao.cor}, {peao.numero}) foi capturada por peça ({peca.cor}, {peca.numero})') #Guias do terminal
                    
                    elif tipo == 'captura_no_percuso_principal': #Se for no caso do percurso
                        if casa_progresso_em_curso == casa_futuro_progresso and peao.cor != peca.cor and peao.posicao != 1: #Se a casa da peça adversária estiver na futura posição do peão do jogador
                            peao.posicao = None #Retorna o peão que estava nas casas principais para a sua base, capturando-o
                            print(f'Peça ({peao.cor}, {peao.numero}) foi capturada por peça ({peca.cor}, {peca.numero})')  #Guias do terminal
     
     #Método que realiza o controle de turno                                                               
    def controle_de_turno(self, tipo, peca=None):
        
        self.dado_status = True #Desbloqueia o dado
        
        if tipo == 'troca_de_turno_pós_jogada': #Caso for a troca de turno pós jogada
                                                        
            if self.resultado_dado != 6: #Se o resultado do dado não for 6, avança para o próximo jogador
                self.turno_atual += 1 #Muda o turno
                
            if self.turno_atual > 3: #Se chegar ao turno de verde
                self.turno_atual = 0 #Volta para o turno do vermelho
                                            
            #Guias do terminal
            print(f'Movimento: peça {peca.cor}, número {peca.numero}')
            print(f'Movimento feito, turno atual é do {self.identificacao_de_turno[self.turno_atual]}')
        
        elif tipo == 'troca_de_turno_por_movimento_indisponivel': #Caso for a troca de turno por movimento indisponível
            
            #Guias do terminal
            print(f'Movimento Indisponivel para {self.identificacao_de_turno[self.turno_atual]}')
            
            self.turno_atual += 1 #Muda o turno
            
            if self.turno_atual > 3: #Se chegar ao turno de verde
                self.turno_atual = 0 #Volta para o turno do vermelho
                            
            #Guias do terminal
            print(f'Logo turno atual é do {self.identificacao_de_turno[self.turno_atual]}')             
            print(' ')
        
    #Método que verifica se há um ganhador da partida
    def verificar_ganhador(self):
        
        #Procura dentro das cores
        for cor, grupo in self.peoes.items():        
            
            if all(peca.posicao == 40 for peca in grupo.values()): #Se todos os peões estiverem na ultima casa especial
                return cor #retorna a cor do grupo
            
        return None #retorna que não há nenhum ganhador
    
    #Método que realiza o fim da partida    
    def fim_da_partida(self):
        self.jogo_encerrado = True #Atribui a variável um valor que indica que tem um ganhador
        self.dado_status = False #Bloqueia o dado para impossibilitar sorteios
        #Guias do terminal
        print('Parabéns!') 
        print(f'O Ganhador dessa partida foi: {self.verificar_ganhador()}.')
        print('Obrigado por Jogar - 2ADS')
    
    #Método que realiza a atualização das músicas    
    def atualizar_musicas(self):
        #Inicia a próxima ou reinicia a playlist
        self.musica_indice = (self.musica_indice + 1) % len(self.musicas) 
        pygame.mixer.music.load(str(self.musicas[self.musica_indice]))
        pygame.mixer.music.play()