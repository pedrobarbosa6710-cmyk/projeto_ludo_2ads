#Importando a biblioteca de python e iniciando a biblioteca
import pygame
from pathlib import Path
pygame.init()

#Tamanho da janela
tela_largura = 900
tela_altura = 760
tela = pygame.display.set_mode((tela_largura, tela_altura))

#Titulo da janela
pygame.display.set_caption('PROJETO LUDO - 2ADS')

#fundo do tabulereiro
cor_fundo = 0, 0, 0
fundo_largura = 700
fundo_altura = 700
fundo_x, fundo_y = (900-fundo_largura)/2, (760-fundo_altura)/2
fundo = pygame.Rect(fundo_x, fundo_y, fundo_largura, fundo_altura)

#Carregar imagem do tabuleiro
caminho_tabuleiro = Path('assets') / 'images' / 'tabuleiro_sprite' / 'tabuleiro_ludo.png'
imagem0 = pygame.image.load(caminho_tabuleiro).convert_alpha()

#Tamanho e cordenadas do tabuleiro
imagem0_x, imagem0_y = imagem0.get_size()
tabuleiro_x = imagem0_x * 10
tabulerio_y = imagem0_y * 10
centro_tabuleiro = (900-tabuleiro_x)/2, (760-tabulerio_y)/2

#Redimensionamento do tabuleiro
tabuleiro = pygame.transform.scale(imagem0, (640, 640))

#caminho e carregar icon do dado
caminho_dado = Path('assets') / 'images' / 'dado_sprite' / 'dado_icon.png'

#tamanho e cordenadas do dado no tabuleiro
imagem_dado = pygame.image.load(caminho_dado).convert_alpha()
icon_dado = pygame.transform.scale(imagem_dado, (64,64))
posicao_dado = 820, 16

#redimensionamento do dado no tabuleiro

#caminho das imagens das peças 
caminho_vermelho = Path('assets') / 'images' / 'peao_sprite' / 'peao_vermelho1.png'
caminho_amarelo = Path('assets') / 'images' / 'peao_sprite' / 'peao_amarelo1.png'
caminho_verde = Path('assets') / 'images' / 'peao_sprite' / 'peao_verde1.png'
caminho_azul = Path('assets') / 'images' / 'peao_sprite' / 'peao_azul1.png'

#carregando as peças
imagem1 = pygame.image.load(caminho_vermelho).convert_alpha()
imagem2 = pygame.image.load(caminho_vermelho).convert_alpha()
imagem3 = pygame.image.load(caminho_vermelho).convert_alpha()
imagem4 = pygame.image.load(caminho_vermelho).convert_alpha()
imagem5 = pygame.image.load(caminho_amarelo).convert_alpha()
imagem6 = pygame.image.load(caminho_amarelo).convert_alpha()
imagem7 = pygame.image.load(caminho_amarelo).convert_alpha()
imagem8 = pygame.image.load(caminho_amarelo).convert_alpha()
imagem9 = pygame.image.load(caminho_verde).convert_alpha()
imagem10 = pygame.image.load(caminho_verde).convert_alpha()
imagem11 = pygame.image.load(caminho_verde).convert_alpha()
imagem12 = pygame.image.load(caminho_verde).convert_alpha()
imagem13 = pygame.image.load(caminho_azul).convert_alpha()
imagem14 = pygame.image.load(caminho_azul).convert_alpha()
imagem15 = pygame.image.load(caminho_azul).convert_alpha()
imagem16 = pygame.image.load(caminho_azul).convert_alpha()

#redimensionando as peças

peao1 = pygame.transform.scale(imagem1, (48, 48))
peao2 = pygame.transform.scale(imagem2, (48, 48))
peao3 = pygame.transform.scale(imagem3, (48, 48))
peao4 = pygame.transform.scale(imagem4, (48, 48))
peao5 = pygame.transform.scale(imagem5, (48, 48))
peao6 = pygame.transform.scale(imagem6, (48, 48))
peao7 = pygame.transform.scale(imagem7, (48, 48))
peao8 = pygame.transform.scale(imagem8, (48, 48))
peao9 = pygame.transform.scale(imagem9, (48, 48))
peao10 = pygame.transform.scale(imagem10, (48, 48))
peao11 = pygame.transform.scale(imagem11, (48, 48))
peao12 = pygame.transform.scale(imagem12, (48, 48))
peao13 = pygame.transform.scale(imagem13, (48, 48))
peao14 = pygame.transform.scale(imagem14, (48, 48))
peao15 = pygame.transform.scale(imagem15, (48, 48))
peao16 = pygame.transform.scale(imagem16, (48, 48))

#cordenadas iniciais no tabuleiro
posicaoinicial_peao1 = 152, 72
posicaoinicial_peao2 = 222, 72
posicaoinicial_peao3 = 152, 142
posicaoinicial_peao4 = 222, 142
posicaoinicial_peao5 = 632, 72
posicaoinicial_peao6 = 702, 72
posicaoinicial_peao7 = 632, 142
posicaoinicial_peao8 = 702, 142
posicaoinicial_peao9 = 152, 542
posicaoinicial_peao10 = 222, 542
posicaoinicial_peao11 = 152, 622
posicaoinicial_peao12 = 222, 622
posicaoinicial_peao13 = 632, 542
posicaoinicial_peao14 = 702, 542
posicaoinicial_peao15 = 632, 622
posicaoinicial_peao16 = 702, 622

#Exercução do programa
jogando = True
cor_do_fundo = 255, 255, 255
while jogando == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogando = False

    #desenha o fundo do tabuleiro        
    tela.fill((cor_do_fundo))
    tela.fill(cor_fundo, fundo)

    #desenha o tabuleiro
    tela.blit(tabuleiro, (centro_tabuleiro))

    #desenha icon dado
    tela.blit(icon_dado, (posicao_dado))

    #desenha as peças vermelhas/amarelas/verdes/azuis
    tela.blit(peao1, posicaoinicial_peao1)
    tela.blit(peao2, posicaoinicial_peao2)
    tela.blit(peao3, posicaoinicial_peao3)
    tela.blit(peao4, posicaoinicial_peao4)
    tela.blit(peao5, posicaoinicial_peao5)
    tela.blit(peao6, posicaoinicial_peao6)
    tela.blit(peao7, posicaoinicial_peao7)
    tela.blit(peao8, posicaoinicial_peao8)
    tela.blit(peao9, posicaoinicial_peao9)
    tela.blit(peao10, posicaoinicial_peao10)
    tela.blit(peao11, posicaoinicial_peao11)
    tela.blit(peao12, posicaoinicial_peao12)
    tela.blit(peao13, posicaoinicial_peao13)
    tela.blit(peao14, posicaoinicial_peao14)
    tela.blit(peao15, posicaoinicial_peao15)
    tela.blit(peao16, posicaoinicial_peao16)

    #atualiza a tela
    pygame.display.flip()

#encerra o programa
pygame.quit()