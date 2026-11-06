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

#icon da janela
caminho_icon = diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_verde2.png'
icon =  pygame.image.load(caminho_icon)
pygame.display.set_icon(icon)

# Biblioteca de Playlist
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

#loop da playlist
indice = 0
fim_musica = pygame.USEREVENT + 1    
pygame.mixer.music.set_endevent(fim_musica)

#exercução das músicas
pygame.mixer.music.load(str(musicas[indice]))
pygame.mixer.music.play()

#fundo e borda do tabulereiro
cor_do_fundo = 0, 200, 0
cor_borda = 0, 0, 0
borda_largura = 700
borda_altura = 700
borda_x, borda_y = (900-borda_largura)/2, (760-borda_altura)/2
borda = pygame.Rect(borda_x, borda_y, borda_largura, borda_altura)

#Carregar imagem do tabuleiro
caminho_tabuleiro = diretorio / 'assets' / 'images' / 'tabuleiro_sprite' / 'tabuleiro_ludo.png'
tabuleiro = pygame.transform.scale(pygame.image.load(caminho_tabuleiro).convert_alpha(), (640, 640))

#Tamanho e cordenadas do tabuleiro
tabuleiro_x, tabuleiro_y = tabuleiro.get_size()
centro_tabuleiro = (900-tabuleiro_x)/2, (760-tabuleiro_y)/2

#caminho, carregar e coordenadas do icon do dado
caminho_dado = diretorio / 'assets' / 'images' / 'icons' / 'dado_icon.png'
dado = pygame.transform.scale(pygame.image.load(caminho_dado).convert_alpha(), (64,64))
posicao_dado = 820, 16

#area cliclavel do icon dado
areaclicavel_dado = pygame.Rect(820, 16, 64, 64)

#Biblioteca para as faces do dado
caminho_facesdado = {
    1: diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face1.png',
    2: diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face2.png',
    3: diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face3.png',
    4: diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face4.png',
    5: diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face5.png',
    6: diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face6.png'
}

imagem_facesdado = {
    1: pygame.transform.scale(pygame.image.load(caminho_facesdado[1]).convert_alpha(), (64, 64)),
    2: pygame.transform.scale(pygame.image.load(caminho_facesdado[2]).convert_alpha(), (64, 64)),
    3: pygame.transform.scale(pygame.image.load(caminho_facesdado[3]).convert_alpha(), (64, 64)),
    4: pygame.transform.scale(pygame.image.load(caminho_facesdado[4]).convert_alpha(), (64, 64)),
    5: pygame.transform.scale(pygame.image.load(caminho_facesdado[5]).convert_alpha(), (64, 64)),
    6: pygame.transform.scale(pygame.image.load(caminho_facesdado[6]).convert_alpha(), (64, 64))
}

#posição da face do dado
posicao_facedado = 820, 80

# caminho, carregar e cordenadas da imagem do 2ADS
caminho_icon2ADS = diretorio / 'assets' / 'images' / 'icons' / '2ADS_icon.png'
imagem_2ADS =  pygame.transform.scale(pygame.image.load(caminho_icon2ADS).convert_alpha(), (64, 64))
posicao_2ADS = 20, 12

#area ciclavel imagem 2ADS
areaclicavel_imagem2ADS = pygame.Rect(20, 12, 64, 64)

# Biblioteca das peças

caminho_imagens_peoes1 = {
    'vermelho': diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_vermelho1.png',
    'amarelo': diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_amarelo1.png',
    'verde': diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_verde1.png',
    'azul': diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_azul1.png'
}

caminho_imagens_peoes2 = {
    'vermelho': diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_vermelho2.png',
    'amarelo': diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_amarelo2.png',
    'verde': diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_verde2.png',
    'azul': diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_azul2.png'
}

imagem_peoes1 = {
    'vermelho': pygame.transform.scale(pygame.image.load(caminho_imagens_peoes1['vermelho']).convert_alpha(), (48, 48)),
    'amarelo': pygame.transform.scale(pygame.image.load(caminho_imagens_peoes1['amarelo']).convert_alpha(), (48, 48)),
    'verde': pygame.transform.scale(pygame.image.load(caminho_imagens_peoes1['verde']).convert_alpha(), (48, 48)),
    'azul': pygame.transform.scale(pygame.image.load(caminho_imagens_peoes1['azul']).convert_alpha(), (48, 48))
}

imagem_peoes2 = {
    'vermelho': pygame.transform.scale(pygame.image.load(caminho_imagens_peoes2['vermelho']).convert_alpha(), (48, 48)),
    'amarelo': pygame.transform.scale(pygame.image.load(caminho_imagens_peoes2['amarelo']).convert_alpha(), (48, 48)),
    'verde': pygame.transform.scale(pygame.image.load(caminho_imagens_peoes2['verde']).convert_alpha(), (48, 48)),
    'azul': pygame.transform.scale(pygame.image.load(caminho_imagens_peoes2['azul']).convert_alpha(), (48, 48))
}

posicao_peoes1 = {
    'vermelho': 
        [(152, 72), (222, 72),
        (152, 142), (222, 142)],

    'amarelo':
       [(632, 72), (702, 72),
        (632, 142), (702, 142)],
         
    'verde': 
        [(152, 542), (222, 542),
        (152, 622), (222, 622)],

    'azul': 
        [(632, 542), (702, 542),
        (632, 622), (702, 622)],
}

posicao_peoes2 = {
    'vermelho': 
        [(0, 0), (0, 0),
        (0, 0), (0, 0)],

    'amarelo':
       [(0, 0), (0, 0),
        (0, 0), (0, 0)],
         
    'verde': 
        [(0, 0), (0, 0),
        (0, 0), (0, 0)],

    'azul': 
        [(0, 0), (0, 0),
        (0, 0), (0, 0)],
}

#Exercução do programa
jogando = True
lado = 0

while jogando == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False
        elif event.type == pygame.MOUSEMOTION:
            if areaclicavel_imagem2ADS.collidepoint(event.pos) or areaclicavel_dado.collidepoint(event.pos):
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)
            else:
                pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if areaclicavel_dado.collidepoint(event.pos):
                lado = randint(1, 6)
            if areaclicavel_imagem2ADS.collidepoint(event.pos):
                webbrowser.open("https://www.instagram.com/2adsistemas/")
        elif event.type == fim_musica:
            indice = (indice + 1) % len(musicas)
            pygame.mixer.music.load(str(musicas[indice]))
            pygame.mixer.music.play()

    #Define o fundo desenha o borda do tabuleiro        
    tela.fill((cor_do_fundo))
    tela.fill(cor_borda, borda)

    #desenha o tabuleiro
    tela.blit(tabuleiro, (centro_tabuleiro))

    #desenha icon dado
    tela.blit(dado, (posicao_dado))
    if lado > 0:
        tela.blit(imagem_facesdado[lado], posicao_facedado)
    
    #desenha icon 2ADS
    tela.blit(imagem_2ADS, (posicao_2ADS))
    
    #desenha as peças vermelhas/amarelas/verdes/azuis
    for cor in posicao_peoes1:
        for posicao in posicao_peoes1[cor]:
            tela.blit(imagem_peoes1[cor], posicao)
                    
    #atualiza a tela
    pygame.display.flip()

#encerra o programa
pygame.quit()