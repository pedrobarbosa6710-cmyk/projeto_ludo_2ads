#Importando a bibliotecas
import pygame

#Função que carrega as imagens
def carregar_recursos(diretorio):
    #Dicionário que indica o caminho das imagens
    caminhos_imagens = {
        'tabuleiro': diretorio / 'assets' / 'images' / 'tabuleiro_sprite' / 'tabuleiro_ludo.png',
    
        'vermelho': [diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_vermelho1.png',
                diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_vermelho2.png' ],
    
        'amarelo': [diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_amarelo1.png',
                diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_amarelo2.png' ],
    
        'verde': [diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_verde1.png',
                diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_verde2.png' ],
    
        'azul': [diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_azul1.png',
                diretorio / 'assets' / 'images' / 'peao_sprite' / 'peao_azul2.png' ],
    
        'icon_dado': diretorio / 'assets' / 'images' / 'icons' / 'dado_icon.png',
    
        'faces_dado': [
            diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face1.png',
            diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face2.png',
            diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face3.png',
            diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face4.png',
            diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face5.png',
            diretorio / 'assets' / 'images' / 'dado_sprite' / 'dado_face6.png'
        ],
    
        'icon_2ads': diretorio / 'assets' / 'images' / 'icons' / '2ADS_icon.png'
    }

    #Dicionario indica as imagens peças
    imagens = {
        'tabuleiro': pygame.transform.scale(pygame.image.load(caminhos_imagens['tabuleiro']).convert_alpha(), (640, 640)),
    
        'vermelho': [pygame.transform.scale(pygame.image.load(caminhos_imagens['vermelho'][0]).convert_alpha(), (48, 48)),
                pygame.transform.scale(pygame.image.load(caminhos_imagens['vermelho'][1]).convert_alpha(), (48, 48))],
    
        'amarelo': [pygame.transform.scale(pygame.image.load(caminhos_imagens['amarelo'][0]).convert_alpha(), (48, 48)),
                pygame.transform.scale(pygame.image.load(caminhos_imagens['amarelo'][1]).convert_alpha(), (48, 48))],
    
        'verde': [pygame.transform.scale(pygame.image.load(caminhos_imagens['verde'][0]).convert_alpha(), (48, 48)),
                pygame.transform.scale(pygame.image.load(caminhos_imagens['verde'][1]).convert_alpha(), (48, 48))],
    
        'azul': [pygame.transform.scale(pygame.image.load(caminhos_imagens['azul'][0]).convert_alpha(), (48, 48)),
                pygame.transform.scale(pygame.image.load(caminhos_imagens['azul'][1]).convert_alpha(), (48, 48))],
    
        'icon_dado': pygame.transform.scale(pygame.image.load(caminhos_imagens['icon_dado']).convert_alpha(), (64,64)),
    
        'faces_dado': {
            1: pygame.transform.scale(pygame.image.load(caminhos_imagens['faces_dado'][0]).convert_alpha(), (64, 64)),
            2: pygame.transform.scale(pygame.image.load(caminhos_imagens['faces_dado'][1]).convert_alpha(), (64, 64)),
            3: pygame.transform.scale(pygame.image.load(caminhos_imagens['faces_dado'][2]).convert_alpha(), (64, 64)),
            4: pygame.transform.scale(pygame.image.load(caminhos_imagens['faces_dado'][3]).convert_alpha(), (64, 64)),
            5: pygame.transform.scale(pygame.image.load(caminhos_imagens['faces_dado'][4]).convert_alpha(), (64, 64)),
            6: pygame.transform.scale(pygame.image.load(caminhos_imagens['faces_dado'][5]).convert_alpha(), (64, 64))
        },
    
        'icon_2ads': pygame.transform.scale(pygame.image.load(caminhos_imagens['icon_2ads']).convert_alpha(), (64, 64))
    }

    #Dicionario que indica a posição das imagens
    posicoes_imagens = {
        'tabuleiro': ((900-640)/2, (760-640)/2),
    
        'icon_dado': (820, 16),
    
        'faces_dado': (820, 80),
    
        'icon_2ads': (20, 12),
    }
    return caminhos_imagens, imagens, posicoes_imagens #Retorna o caminho, as imagens e suas posições