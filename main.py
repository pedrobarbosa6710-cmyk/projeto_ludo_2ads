# PROJETO JOGO LUDO FEITO EM PYTHON 2ADS
# O comentário que tiver "*" é algo recém adicionado ou que ainda não é difinitivo
# Programador: Pedro Gabriel

#Importando a bibliotecas
import pygame
import webbrowser
from random import shuffle, randint
from pathlib import Path

#Iniciando bibliotecas
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.025)

#Resolvendo problemas do diretorio
diretorio = Path(__file__).resolve().parent

#Tamanho da janela
tela_largura = 900
tela_altura = 760
tela = pygame.display.set_mode((tela_largura, tela_altura))

#Titulo da janela
pygame.display.set_caption('PROJETO LUDO - 2ADS')

#Icon da janela
caminho_icon = diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_verde2.png'
icon =  pygame.image.load(caminho_icon)
pygame.display.set_icon(icon)

#Biblioteca de Playlist
musicas = [
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
shuffle(musicas)

#Loop da playlist
musica_indice = 0
evento_fim_musica = pygame.USEREVENT + 1    
pygame.mixer.music.set_endevent(evento_fim_musica)

#Exercução das músicas
pygame.mixer.music.load(str(musicas[musica_indice]))
pygame.mixer.music.play()

#Fundo e borda do tabulereiro
cor_do_fundo = 0, 200, 0
cor_borda = 0, 0, 0
borda_largura = 700
borda_altura = 700
borda_x, borda_y = (900-borda_largura)/2, (760-borda_altura)/2
borda = pygame.Rect(borda_x, borda_y, borda_largura, borda_altura)

#Carregar imagem do tabuleiro
caminho_tabuleiro = diretorio / 'assets' / 'images' / 'tabuleiro_sprite' / 'tabuleiro_ludo.png'
imagem_tabuleiro = pygame.transform.scale(pygame.image.load(caminho_tabuleiro).convert_alpha(), (640, 640))

#Tamanho e cordenadas do tabuleiro
tabuleiro_x, tabuleiro_y = imagem_tabuleiro.get_size()
posicao_tabuleiro = (900-tabuleiro_x)/2, (760-tabuleiro_y)/2

#Caminho, carregar e coordenadas do icon do dado
caminho_dado = diretorio / 'assets' / 'images' / 'icons' / 'dado_icon.png'
imagem_dado = pygame.transform.scale(pygame.image.load(caminho_dado).convert_alpha(), (64,64))
posicao_dado = 820, 16

#Área cliclavel do icon dado
area_clicavel_dado = pygame.Rect(820, 16, 64, 64)

#Dicionarios para as faces do dado
caminho_faces_dado = {
    1: diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face1.png',
    2: diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face2.png',
    3: diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face3.png',
    4: diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face4.png',
    5: diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face5.png',
    6: diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face6.png'
}

imagem_faces_dado = {
    1: pygame.transform.scale(pygame.image.load(caminho_faces_dado[1]).convert_alpha(), (64, 64)),
    2: pygame.transform.scale(pygame.image.load(caminho_faces_dado[2]).convert_alpha(), (64, 64)),
    3: pygame.transform.scale(pygame.image.load(caminho_faces_dado[3]).convert_alpha(), (64, 64)),
    4: pygame.transform.scale(pygame.image.load(caminho_faces_dado[4]).convert_alpha(), (64, 64)),
    5: pygame.transform.scale(pygame.image.load(caminho_faces_dado[5]).convert_alpha(), (64, 64)),
    6: pygame.transform.scale(pygame.image.load(caminho_faces_dado[6]).convert_alpha(), (64, 64))
}

#Posição da face do dado
posicao_faces_dado = 820, 80

#Caminho, carregar e cordenadas da imagem do 2ADS
caminho_icon_2ads = diretorio / 'assets' / 'images' / 'icons' / '2ADS_icon.png'
imagem_2ads =  pygame.transform.scale(pygame.image.load(caminho_icon_2ads).convert_alpha(), (64, 64))
posicao_2ads = 20, 12

#Área ciclavel imagem 2ADS
area_clicavel_imagem_2ads = pygame.Rect(20, 12, 64, 64)

#Dicionario das casas e coordenadas do tabuleiro
casas_das_bases_tabuleiro = {
    "base_vermelho": {
        1: (152, 72),
        2: (222, 72),
        3: (152, 142),
        4: (222, 142)
    },

    "base_amarelo": {
        1: (632, 72),
        2: (702, 72),
        3: (632, 142),
        4: (702, 142)
    },

    "base_verde": {
        1: (152, 542),
        2: (222, 542),
        3: (152, 622),
        4: (222, 622)
    },

    "base_azul": {
        1: (632, 542),
        2: (702, 542),
        3: (632, 622),
        4: (702, 622)
    }
}

casas_de_entrada = {
    'vermelho': 1,
    'amarelo': 10,
    'verde': 28,
    'azul': 19
}

casas_do_percurso_tabuleiro = {
    1: (132, 282),  #Inicio das vermelhas
    2: (192, 282),
    3: (252, 282),
    4: (312, 282),
    5: (362, 232),
    6: (362, 172),
    7: (362, 112),
    8: (362, 52),
    9: (422, 52),
    10: (492, 52),  #inicio das amarelas
    11: (492, 112),
    12: (492, 172),
    13: (492, 232),
    14: (542, 282),
    15: (602, 282),
    16: (662, 282),
    17: (722, 282),
    18: (722, 342),
    19: (722, 402), # incio das azuis
    20: (662, 402), 
    21: (602, 402),
    22: (542, 402),
    23: (492, 462),
    24: (492, 522),
    25: (492, 582),
    26: (492, 642),
    27: (422, 642),
    28: (362, 642), # inicio das verdes
    29: (362, 582),
    30: (362, 522),
    31: (362, 462),
    32: (312, 402),
    33: (252, 402),
    34: (192, 402),
    35: (132, 402),
    36: (132, 342)
}

casas_finais_tabuleiro = {
    "final_vermelho": {
        1: (192, 342),
        2: (252, 342),
        3: (312, 342),
        4: (382, 342)
    },

    "final_amarelo": {
        1: (422, 112),
        2: (422, 172),
        3: (422, 232),
        4: (422, 302)
    },

    "final_verde": {
        1: (422, 582),
        2: (422, 522),
        3: (422, 462),
        4: (422, 382)
    },

    "final_azul": {
        1: (662, 342),
        2: (602, 342),
        3: (542, 342),
        4: (472, 342)
    }
}

#Dicionario das peças
caminho_imagens_peoes_1 = {
    'vermelho': diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_vermelho1.png',
    'amarelo': diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_amarelo1.png',
    'verde': diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_verde1.png',
    'azul': diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_azul1.png'
}

caminho_imagens_peoes_2 = {
    'vermelho': diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_vermelho2.png',
    'amarelo': diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_amarelo2.png',
    'verde': diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_verde2.png',
    'azul': diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_azul2.png'
}

imagem_peoes_1 = {
    'vermelho': pygame.transform.scale(pygame.image.load(caminho_imagens_peoes_1['vermelho']).convert_alpha(), (48, 48)),
    'amarelo': pygame.transform.scale(pygame.image.load(caminho_imagens_peoes_1['amarelo']).convert_alpha(), (48, 48)),
    'verde': pygame.transform.scale(pygame.image.load(caminho_imagens_peoes_1['verde']).convert_alpha(), (48, 48)),
    'azul': pygame.transform.scale(pygame.image.load(caminho_imagens_peoes_1['azul']).convert_alpha(), (48, 48))
}

imagem_peoes_2 = {
    'vermelho': pygame.transform.scale(pygame.image.load(caminho_imagens_peoes_2['vermelho']).convert_alpha(), (48, 48)),
    'amarelo': pygame.transform.scale(pygame.image.load(caminho_imagens_peoes_2['amarelo']).convert_alpha(), (48, 48)),
    'verde': pygame.transform.scale(pygame.image.load(caminho_imagens_peoes_2['verde']).convert_alpha(), (48, 48)),
    'azul': pygame.transform.scale(pygame.image.load(caminho_imagens_peoes_2['azul']).convert_alpha(), (48, 48))
}

posicao_peoes_1 = {
    'vermelho': [None, None, None, None],

    'amarelo': [None, None, None, None],
         
    'verde': [None, None, None, None],

    'azul': [None, None, None, None],
}

posicao_peoes_2 = {
    'vermelho': [None, None, None, None],

    'amarelo': [None, None, None, None],
         
    'verde': [None, None, None, None],

    'azul': [None, None, None, None],
}

#Váriaveis de exercução e funcionamento
jogo_ativo = True
dado_status = True
resultado_dado = 0

#Dicionario para a identificação dos turnos dos jogadores
identificacao_de_turno = {
    1: 'vermelho',
    2: 'amarelo',
    3: 'verde',
    4: 'azul'
}

#Idenficação do turno atual
turno_atual = 1

#Função que relaciona a posição lógica da peça com a coordenada dela, retorna as coordenadas correspondentes
def coordenadas_peao(cor, numero):
    
    #Onde a peça está atualmente
    progresso = posicao_peoes_1[cor][numero]
    
    #Caso esteja na base
    if progresso is None:
        return casas_das_bases_tabuleiro[f'base_{cor}'][numero + 1]
    
    #Caso esteja no percurso
    elif progresso <= 36:
        casa_real = ((casas_de_entrada[cor] + progresso - 2) % 36) + 1
        return casas_do_percurso_tabuleiro[casa_real]
    
    #Caso esteja na reta final
    elif progresso <= 40:
        return casas_finais_tabuleiro[f'final_{cor}'][progresso - 36]
    
#Função que verifica se há possibilidade de uma peça ser movida, retorna "True" ou "False"
def movimento_valido(cor, numero):
    
    #Onde a peça está atualmente
    progresso = posicao_peoes_1[cor][numero]
    
    #Caso o jogador ainda não tenha girado o dado e não for o seu turno.
    if dado_status == True or identificacao_de_turno[turno_atual] != cor:
        return False
    
    #Caso a peça em que o jogador cliclou ainda estiver na base, verifica se o resultado é igual a 6
    if progresso is None:
        return  resultado_dado == 6
    
    #Caso a peça em que o jogador clicou estiver no percurso
    elif progresso <= 36:
        nova_posicao = progresso + resultado_dado

        #Verifca se a sua possível nova posição ainda está no percurso
        if nova_posicao <= 36:
            return True
        
        #Verifica e limita o peão ao entrar na reta final ficar apenas na primeria casa especial
        return nova_posicao == 37

    #Caso a peça em que o jogador clicou esteja na reta final, compara se a casa especial corresponde ao resultado tirado, válida ou inválida a movimentação
    elif progresso < 40:
        proxima_casa = progresso - 35
        return resultado_dado == proxima_casa
    
    return False

#Loop para exercução do programa
while jogo_ativo == True:
    
    #Define o fundo desenha o borda do tabuleiro        
    tela.fill((cor_do_fundo))
    tela.fill(cor_borda, borda)

    #desenha o tabuleiro
    tela.blit(imagem_tabuleiro, (posicao_tabuleiro))

    #desenha icon dado
    tela.blit(imagem_dado, (posicao_dado))
    if resultado_dado > 0:
        tela.blit(imagem_faces_dado[resultado_dado], posicao_faces_dado)
    
    #desenha icon 2ADS
    tela.blit(imagem_2ads, (posicao_2ads))
    
    #desenha as peças vermelhas/amarelas/verdes/azuis
    for cor in posicao_peoes_1:
        for numero, progresso in enumerate(posicao_peoes_1[cor]):
            coordenadas = coordenadas_peao(cor, numero)
            tela.blit(imagem_peoes_1[cor], coordenadas)
            
    #Detectar eventos e realizar ações
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_ativo = False
            
        #Detecta se o mouse passou por cima de algo interativo e muda o desenho do ponteiro
        elif event.type == pygame.MOUSEMOTION:
            if area_clicavel_imagem_2ads.collidepoint(event.pos) or area_clicavel_dado.collidepoint(event.pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
                
        #Detecta clique do mouse
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            #Funcionamento dos peões
            for cor in posicao_peoes_1:
                
                #Criação de uma área clicavel para cada peão
                for numero, progresso in enumerate(posicao_peoes_1[cor]):
                    area_clicavel_peao = imagem_peoes_1[cor].get_rect()
                    area_clicavel_peao.topleft = coordenadas_peao(cor, numero)
                    area_clicavel_peao_cor = cor
                    
                    #identificação de clique sobre cada peão
                    if area_clicavel_peao.collidepoint(event.pos):
                        
                        #verifica se o clique pode exercer um movimento e se ele é valido
                        if movimento_valido(cor, numero):
                            
                            #caso a peça esteja na base, entra na primeira casa do seu percurso.
                            if posicao_peoes_1[cor][numero] is None:
                                posicao_peoes_1[cor][numero] = 1

                            #Caso a peça esteja no trajeto, movimenta a peça
                            elif posicao_peoes_1[cor][numero] <= 36:
                                posicao_peoes_1[cor][numero] += resultado_dado

                            #Caso ele esteja em um casa especial, sendo válido, avança para a próxima
                            else:
                                posicao_peoes_1[cor][numero] += 1
                            
                            #Desbloqueia o dado
                            dado_status = True
                            
                            #Muda o turno
                            turno_atual += 1
                            
                            #Ao chegar no turno azul, volta para o vermelho
                            if turno_atual > 4:
                                turno_atual = 1
                        
                            #Guias do terminal
                            print(f'Movimento feito, turno atual é do {identificacao_de_turno[turno_atual]}')
                            print(f'Movimento: peça {cor}, número {numero + 1}')
                                                
            #Caso clique em cima do dado, gera um número de 1-6
            if dado_status and area_clicavel_dado.collidepoint(event.pos):
                
                #Sorteia o número de 1-6
                resultado_dado = randint(1, 6)
                
                #Bloqueia o dado
                #(Para um jogador não jogar duas vezes)
                dado_status = False
                
                #Guias do terminal
                print(' ')
                print(f'Resultado do dado foi: {resultado_dado}')
                print(f'Dado bloqueado')

                #Caso o jogador não tenha nenhum movimento disponível, passa o turno
                movimento_disponivel = any(
                    movimento_valido(cor, numero)
                    for cor in posicao_peoes_1
                   for numero in range(4)
                )

                #Se não tiver nenhuma peça fora da base, muda o turno para o próximo jogador
                if not movimento_disponivel:
                    print(f'Movimento Indisponivel para {identificacao_de_turno[turno_atual]}')
                    
                    #Desbloqueia o dado
                    dado_status = True
                    
                    #Muda o turno
                    turno_atual += 1
                    
                    #Ao chegar no turno azul, volta para o vermelho
                    if turno_atual > 4:
                        turno_atual = 1
                        
                #Guias do terminal
                print(f'Logo turno atual é do {identificacao_de_turno[turno_atual]}')             
                print(' ')

                
            #Caso clique em cima do icon 2ads, leva para o instagram da sala
            if area_clicavel_imagem_2ads.collidepoint(event.pos):
                webbrowser.open("https://www.instagram.com/2adsistemas/")
                
                    
        #Execução e loop das músicas do jogo
        elif event.type == evento_fim_musica:
            musica_indice = (musica_indice + 1) % len(musicas)
            pygame.mixer.music.load(str(musicas[musica_indice]))
            pygame.mixer.music.play()
            
    #atualiza a tela
    pygame.display.flip()

#encerra o programa
pygame.quit()