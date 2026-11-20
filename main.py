# PROJETO JOGO LUDO FEITO EM PYTHON 2ADS
# Programador: Pedro Gabriel

#Importando a bibliotecas
import pygame
from pathlib import Path

from classes.jogo import Jogo #Importa classe jogo 
from classes.interface import Interface #Importa classe interface
from sistemas.recursos import carregar_recursos #Importa função de carregar recursos
from sistemas.tabuleiro import casas_do_tabuleiro #Importa dicionário das posições das casas do tabuleiro

#Iniciando bibliotecas
pygame.init()
pygame.mixer.init()
pygame.mixer.music.set_volume(0.050)

#Resolvendo problemas do diretorio
diretorio = Path(__file__).resolve().parent

#Cria o objeto do Jogo
#A tela é criada antes do carregamento das imagens, pois convert_alpha() depende do modo de vídeo
jogo = Jogo(900, 760, 'LUDO ARCÂNIA', 'inicio', casas_do_tabuleiro)

#Carrega os caminhos, imagens e posições das imagens
caminhos_imagens, imagens, posicoes_imagens, musicas, efeitos_sonoros = carregar_recursos(diretorio, jogo)

jogo.configurar_audio(musicas, efeitos_sonoros)

jogo.criar_peoes(imagens) #Executa função para criar os peões

jogo.icon = imagens['verde'][1] #Indica o favicon utilizado na tela

pygame.display.set_icon(jogo.icon) #Define esse mesmo icone como o favicon

interface = Interface(jogo, imagens, posicoes_imagens) #Cria o objeto da Interface

#Loop para exercução do programa
while jogo.jogo_ativo == True:

    interface.desenho_imagens() #Chama o metodo que desenha tabuleiro e icones

    jogo.processar_eventos(pygame.event.get(), interface) #Chama o metodo que processa os eventos

    pygame.display.flip() #atualiza a tela
    jogo.relogio.tick(60) #Limita o jogo para 60FPS

#encerra o programa
pygame.quit()