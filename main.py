# PROJETO JOGO LUDO FEITO EM PYTHON 2ADS
# O comentário que tiver "*" é algo recém adicionado ou que ainda não é difinitivo
# Programador: Pedro Gabriel

#Importando a bibliotecas
import pygame
from random import shuffle
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

#fundo do tabulereiro
cor_fundo = 0, 0, 0
fundo_largura = 700
fundo_altura = 700
fundo_x, fundo_y = (900-fundo_largura)/2, (760-fundo_altura)/2
fundo = pygame.Rect(fundo_x, fundo_y, fundo_largura, fundo_altura)

#Carregar imagem do tabuleiro
caminho_tabuleiro = diretorio / 'assets' / 'images' / 'tabuleiro_sprite' / 'tabuleiro_ludo.png'
imagem0 = pygame.image.load(caminho_tabuleiro).convert_alpha()

#Tamanho e cordenadas do tabuleiro
imagem0_x, imagem0_y = imagem0.get_size()
tabuleiro_x = imagem0_x * 10
tabulerio_y = imagem0_y * 10
centro_tabuleiro = (900-tabuleiro_x)/2, (760-tabulerio_y)/2

#Redimensionamento do tabuleiro
tabuleiro = pygame.transform.scale(imagem0, (640, 640))

# caminho e carregar icon do dado
caminho_dado = diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_icon.png'
imagem_dado = pygame.image.load(caminho_dado).convert_alpha()

# tamanho e cordenadas do dado no tabuleiro
icon_dado = pygame.transform.scale(imagem_dado, (64,64))
posicao_dado = 820, 16

# caminho e carregar a imagem do 2ADS
caminho_icon2ADS = diretorio / 'assets' / 'images' / 'icons' / '2ADS_icon.png'
imagem_2ADS = pygame.image.load(caminho_icon2ADS).convert_alpha()

# tamanho e cordenadas
icon_2ADS = pygame.transform.scale(imagem_2ADS, (64, 64))
posicao_2ADS = 20, 12

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
cor_do_fundo = 255, 255, 255
while jogando == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False
        elif event.type == fim_musica:
            indice_da_musica = (indice + 1) % len(musicas)
            pygame.mixer.music.load(str(musicas[indice]))
            pygame.mixer.music.play()

    #desenha o fundo do tabuleiro        
    tela.fill((cor_do_fundo))
    tela.fill(cor_fundo, fundo)

    #desenha o tabuleiro
    tela.blit(tabuleiro, (centro_tabuleiro))

    #desenha icon dado
    tela.blit(icon_dado, (posicao_dado))

    #desenha icon 2ADS
    tela.blit(icon_2ADS, (posicao_2ADS))

    # desenha as peças vermelhas/amarelas/verdes/azuis
    for cor in posicao_peoes1:
        for posicao in posicao_peoes1[cor]:
            tela.blit(imagem_peoes1[cor], posicao)
                    
    #atualiza a tela
    pygame.display.flip()

#encerra o programa
pygame.quit()