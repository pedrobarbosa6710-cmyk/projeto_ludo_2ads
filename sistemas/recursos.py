#Importando a bibliotecas
import pygame

#Função que carrega as imagens
def carregar_recursos(diretorio, jogo):
        
        #Dicionário que indica o caminho das imagens
        caminhos_imagens = {
        
                #FUNDOS
                'fundo_alternativo': diretorio / 'assets' / 'images' / 'fundos' / 'fundo_alternativo.png',
                'fundo_padrao': diretorio / 'assets' / 'images' / 'fundos' / 'fundo_padrao.png',
                'fundo_escuro': diretorio / 'assets' / 'images' / 'fundos' / 'fundo_escuro.png',
                
                #TEXTOS
                'titulo_inicio': diretorio / 'assets' / 'images' / 'textos' / 'titulo_inicio.png',
                'tela_de_creditos': diretorio / 'assets' / 'images' / 'textos' / 'tela_de_creditos.png',               
                'fundo_confirmacao': diretorio / 'assets' / 'images' / 'textos' / 'painel_confirmacao.png',
                'vencedor_vermelho': diretorio / 'assets' / 'images' / 'textos' / 'vencedor_vermelho.png',
                'vencedor_amarelo': diretorio / 'assets' / 'images' / 'textos' / 'vencedor_amarelo.png',
                'vencedor_azul': diretorio / 'assets' / 'images' / 'textos' / 'vencedor_azul.png',
                'vencedor_verde': diretorio / 'assets' / 'images' / 'textos' / 'vencedor_verde.png',
                
                #TABULEIRO E PEÇAS
                'tabuleiro': diretorio / 'assets' / 'images' / 'tabuleiro_sprite' / 'tabuleiro_ludo.png',
                'vermelho': [diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_vermelho1.png',
                        diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_vermelho2.png' ],
                'amarelo': [diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_amarelo1.png',
                        diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_amarelo2.png' ],
                'verde': [diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_verde1.png',
                        diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_verde2.png' ],
                'azul': [diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_azul1.png',
                        diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_azul2.png' ],

                #ICONES E BOTÕES
                'icon_dado': diretorio / 'assets' / 'images' / 'icons_e_botoes' / 'dado_icon.png',
                'faces_dado': [
                diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face1.png',
                diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face2.png',
                diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face3.png',
                diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face4.png',
                diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face5.png',
                diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face6.png'
                ],
                'icon_2ads': diretorio / 'assets' / 'images' / 'icons_e_botoes' / '2ADS_icon.png',
                'icon_turno': diretorio / 'assets' / 'images' / 'icons_e_botoes' / 'icon_turno.png',
                'icon_cadeado': diretorio / 'assets' / 'images' / 'icons_e_botoes' / 'icon_cadeado.png', 
                'botao_jogar': diretorio / 'assets' / 'images' / 'icons_e_botoes' / 'botao_jogar_inicio.png',
                'botao_jogar_alternativo': diretorio / 'assets' / 'images' / 'icons_e_botoes' / 'botao_jogar_inicio_alternativo.png',
                'botao_creditos': diretorio / 'assets' / 'images' / 'icons_e_botoes' / 'botao_creditos_inicio.png',
                'botao_creditos_alternativo': diretorio / 'assets' / 'images' / 'icons_e_botoes' / 'botao_creditos_inicio_alternativo.png',
                'botao_voltar_para_inicio': diretorio / 'assets' / 'images' / 'icons_e_botoes' / 'botao_voltar_para_inicio.png',   
                'botao_voltar_para_inicio_alternativo': diretorio / 'assets' / 'images' / 'icons_e_botoes' / 'botao_voltar_para_inicio_alternativo.png',
                'botao_voltar': diretorio / 'assets' / 'images' / 'icons_e_botoes' / 'botao_voltar.png',
                'botao_sair': diretorio / 'assets' / 'images' / 'icons_e_botoes' / 'botao_sair.png',
                'botao_confirmacao': diretorio / 'assets' / 'images' / 'icons_e_botoes' / 'botao_confirmar.png',
                'botao_cancelar': diretorio / 'assets' / 'images' / 'icons_e_botoes' / 'botao_cancelar.png',
                'botao_confirmacao_alternativo': diretorio / 'assets' / 'images' / 'icons_e_botoes' / 'botao_confirmar_alternativo.png',
                'botao_cancelar_alternativo': diretorio / 'assets' / 'images' / 'icons_e_botoes' / 'botao_cancelar_alternativo.png'
        }
        #Dicionario indica as imagens peças
        imagens = {
                
                #FUNDOS
                'fundo_alternativo': pygame.transform.scale(pygame.image.load(caminhos_imagens['fundo_alternativo']).convert_alpha(), (900, 760)),
                'fundo_padrao': pygame.transform.scale(pygame.image.load(caminhos_imagens['fundo_padrao']).convert_alpha(), (900, 760)),
                'fundo_escuro': pygame.transform.scale(pygame.image.load(caminhos_imagens['fundo_escuro']).convert_alpha(), (900, 760)),
                
                #TEXTOS
                'fundo_confirmacao': pygame.transform.scale(pygame.image.load(caminhos_imagens['fundo_confirmacao']).convert_alpha(), (720, 216)),
                'titulo_inicio': pygame.transform.scale(pygame.image.load(caminhos_imagens['titulo_inicio']).convert_alpha(), (600, 350)),
                'tela_de_creditos': pygame.transform.scale(pygame.image.load(caminhos_imagens['tela_de_creditos']).convert_alpha(), (700,700)),
                'vencedor': {
                        'vermelho': pygame.transform.scale(pygame.image.load(caminhos_imagens['vencedor_vermelho']).convert_alpha(), (200, 75)),
                        'amarelo': pygame.transform.scale(pygame.image.load(caminhos_imagens['vencedor_amarelo']).convert_alpha(), (200, 75)),
                        'azul': pygame.transform.scale(pygame.image.load(caminhos_imagens['vencedor_azul']).convert_alpha(), (200, 75)),
                        'verde': pygame.transform.scale(pygame.image.load(caminhos_imagens['vencedor_verde']).convert_alpha(), (200, 75)),      
                },
                
                #PEÇAS E TABULEIRO
                'tabuleiro': pygame.transform.scale(pygame.image.load(caminhos_imagens['tabuleiro']).convert_alpha(), (640, 640)),
                'vermelho': [pygame.transform.scale(pygame.image.load(caminhos_imagens['vermelho'][0]).convert_alpha(), (48, 48)),
                        pygame.transform.scale(pygame.image.load(caminhos_imagens['vermelho'][1]).convert_alpha(), (48, 48))],
                'amarelo': [pygame.transform.scale(pygame.image.load(caminhos_imagens['amarelo'][0]).convert_alpha(), (48, 48)),
                        pygame.transform.scale(pygame.image.load(caminhos_imagens['amarelo'][1]).convert_alpha(), (48, 48))],
                'verde': [pygame.transform.scale(pygame.image.load(caminhos_imagens['verde'][0]).convert_alpha(), (48, 48)),
                        pygame.transform.scale(pygame.image.load(caminhos_imagens['verde'][1]).convert_alpha(), (48, 48))],
                'azul': [pygame.transform.scale(pygame.image.load(caminhos_imagens['azul'][0]).convert_alpha(), (48, 48)),
                        pygame.transform.scale(pygame.image.load(caminhos_imagens['azul'][1]).convert_alpha(), (48, 48))],
                
                
                #ICONES e BOTÕES
                'icon_dado': pygame.transform.scale(pygame.image.load(caminhos_imagens['icon_dado']).convert_alpha(), (64,64)),
                'faces_dado': {
                1: pygame.transform.scale(pygame.image.load(caminhos_imagens['faces_dado'][0]).convert_alpha(), (64, 64)),
                2: pygame.transform.scale(pygame.image.load(caminhos_imagens['faces_dado'][1]).convert_alpha(), (64, 64)),
                3: pygame.transform.scale(pygame.image.load(caminhos_imagens['faces_dado'][2]).convert_alpha(), (64, 64)),
                4: pygame.transform.scale(pygame.image.load(caminhos_imagens['faces_dado'][3]).convert_alpha(), (64, 64)),
                5: pygame.transform.scale(pygame.image.load(caminhos_imagens['faces_dado'][4]).convert_alpha(), (64, 64)),
                6: pygame.transform.scale(pygame.image.load(caminhos_imagens['faces_dado'][5]).convert_alpha(), (64, 64))
                },
                'icon_2ads': pygame.transform.scale(pygame.image.load(caminhos_imagens['icon_2ads']).convert_alpha(), (64, 64)),
                'icon_turno':  pygame.transform.scale(pygame.image.load(caminhos_imagens['icon_turno']).convert_alpha(), (64, 64)),
                'icon_cadeado':  pygame.transform.scale(pygame.image.load(caminhos_imagens['icon_cadeado']).convert_alpha(), (32, 32)),
                'botao_voltar_para_inicio_alternativo': diretorio / 'assets' / 'images' / 'titulos_e_botoes' / 'botao_voltar_para_inicio_alternativo.png',   
                'botao_jogar': [pygame.transform.scale(pygame.image.load(caminhos_imagens['botao_jogar']).convert_alpha(), (300, 100)),
                                pygame.transform.scale(pygame.image.load(caminhos_imagens['botao_jogar_alternativo']).convert_alpha(), (300, 100))],
                'botao_creditos': [pygame.transform.scale(pygame.image.load(caminhos_imagens['botao_creditos']).convert_alpha(), (300, 100)),
                                   pygame.transform.scale(pygame.image.load(caminhos_imagens['botao_creditos_alternativo']).convert_alpha(), (300, 100))],
                'botao_voltar_para_inicio': [pygame.transform.scale(pygame.image.load(caminhos_imagens['botao_voltar_para_inicio']).convert_alpha(), (300, 100)),
                                   pygame.transform.scale(pygame.image.load(caminhos_imagens['botao_voltar_para_inicio_alternativo']).convert_alpha(), (300, 100))],
                'botao_confirmacao': [pygame.transform.scale(pygame.image.load(caminhos_imagens['botao_confirmacao']).convert_alpha(), (300, 90)),
                                      pygame.transform.scale(pygame.image.load(caminhos_imagens['botao_confirmacao_alternativo']).convert_alpha(), (300, 90))],
                'botao_cancelar': [pygame.transform.scale(pygame.image.load(caminhos_imagens['botao_cancelar']).convert_alpha(), (300, 90)),
                                   pygame.transform.scale(pygame.image.load(caminhos_imagens['botao_cancelar_alternativo']).convert_alpha(), (300, 90))],
                'botao_voltar': pygame.transform.scale(pygame.image.load(caminhos_imagens['botao_voltar']).convert_alpha(), (64,64)),
                'botao_sair': pygame.transform.scale(pygame.image.load(caminhos_imagens['botao_sair']).convert_alpha(), (48,48))
        }

        #Dicionario que indica a posição das imagens
        posicoes_imagens = {
                #FUNDOS 
                'fundos': (0,0),
                'fundo_confirmacao': (90, 250),
                
                #TEXTOS:
                'titulo_inicio': ((jogo.tela_largura-600)/2, 50),
                'vencedor': ((jogo.tela_largura-200)/2 , jogo.tela_altura-330),
                'tela_de_creditos': ((jogo.tela_largura-700)/2, (jogo.tela_altura-700)/2),
                'peca_vencedora': (((jogo.tela_largura-320)/2), ((jogo.tela_altura-550)/2)),
                
                #TABULEIRO
                'tabuleiro': ((jogo.tela_largura-640)/2, (jogo.tela_altura-640)/2),

                #BOTÕES 
                'icon_dado': (jogo.tela_largura-80, jogo.tela_altura-744),
                'icon_turno': (jogo.tela_largura-884, jogo.tela_altura-744),
                'icon_cadeado': (jogo.tela_largura-48, jogo.tela_altura-744),
                'icon_peca_turno': (jogo.tela_largura-876, jogo.tela_altura-680),
                'faces_dado': (jogo.tela_largura-80, jogo.tela_altura-680),
                'icon_2ads': (jogo.tela_largura-884, jogo.tela_altura-80),
                'botao_jogar': ((jogo.tela_largura-300)/2, 400),      
                'botao_creditos': ((jogo.tela_largura-300)/2, 525),
                'botao_voltar_para_inicio': ((jogo.tela_largura-300)/2 , jogo.tela_altura-230),
                'botao_voltar': (jogo.tela_largura-884, jogo.tela_altura-744), 
                'botao_sair': (jogo.tela_largura-80, jogo.tela_altura-64),
                'botao_confirmacao': (140, 430),
                'botao_cancelar': (470, 430),
        }
        
        #Lista de Playlist
        musicas = [
                diretorio / 'assets' / 'sounds' / 'musicas' / 'faixa_1.mp3',
                diretorio / 'assets' / 'sounds' / 'musicas' / 'faixa_2.mp3',
                diretorio / 'assets' / 'sounds' / 'musicas' / 'faixa_3.mp3',
                diretorio / 'assets' / 'sounds' / 'musicas' / 'faixa_4.mp3',
                diretorio / 'assets' / 'sounds' / 'musicas' / 'faixa_5.mp3',
                diretorio / 'assets' / 'sounds' / 'musicas' / 'faixa_6.mp3',
                diretorio / 'assets' / 'sounds' / 'musicas' / 'faixa_7.mp3',
                diretorio / 'assets' / 'sounds' / 'musicas' / 'faixa_8.mp3',
                diretorio / 'assets' / 'sounds' / 'musicas' / 'faixa_9.mp3',
                diretorio / 'assets' / 'sounds' / 'musicas' / 'faixa_10.mp3'
        ]
        
        #Dicionário dos efeitos sonoros
        efeitos_sonoros = {
                'efeito_de_clique': pygame.mixer.Sound(diretorio / 'assets' / 'sounds' / 'efeitos_sonoros' / 'efeito_de_clique.mp3'),
                'efeito_movimento_peca': pygame.mixer.Sound(diretorio / 'assets' / 'sounds' / 'efeitos_sonoros' / 'efeito_movimento_peca.mp3'),
                'efeito_ao_jogar_dado': pygame.mixer.Sound(diretorio / 'assets' / 'sounds' / 'efeitos_sonoros' / 'efeito_ao_jogar_dado.mp3')
        }
                
        return caminhos_imagens, imagens, posicoes_imagens, musicas, efeitos_sonoros #Retorna o caminho, as imagens e suas posições