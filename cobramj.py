import pygame
import random

# Cores
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)

# Dimensões da janela
largura_janela = 800
altura_janela = 600

# Tamanho dos pixels
tamanho_pixel = 10

# Inicialização do Pygame
pygame.init()

# Criação da janela
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption('Cobra Pixelada')

# Relógio para controle de FPS
clock = pygame.time.Clock()

# Função para desenhar a cobra
def desenhar_cobra(cobra):
    for pixel in cobra:
        pygame.draw.rect(janela, VERDE, (pixel[0], pixel[1], tamanho_pixel, tamanho_pixel))

# Função principal do jogo
def jogo():
    fim_de_jogo = False

    # Posição inicial da cobra
    cobra = [[200, 200], [210, 200], [220, 200]]

    # Direção inicial da cobra
    direcao = "direita"

    while not fim_de_jogo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fim_de_jogo = True

            # Controle da cobra
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and direcao != "direita":
                    direcao = "esquerda"
                elif event.key == pygame.K_RIGHT and direcao != "esquerda":
                    direcao = "direita"
                elif event.key == pygame.K_UP and direcao != "baixo":
                    direcao = "cima"
                elif event.key == pygame.K_DOWN and direcao != "cima":
                    direcao = "baixo"

        # Movimento da cobra
        if direcao == "direita":
            cobra[0][0] += tamanho_pixel
        elif direcao == "esquerda":
            cobra[0][0] -= tamanho_pixel
        elif direcao == "cima":
            cobra[0][1] -= tamanho_pixel
        elif direcao == "baixo":
            cobra[0][1] += tamanho_pixel

        # Verificar se a cobra bateu na parede
        if cobra[0][0] >= largura_janela or cobra[0][0] < 0 or cobra[0][1] >= altura_janela or cobra[0][1] < 0:
            fim_de_jogo = True

        # Criação de uma nova cobra com base na posição atual
        nova_cobra = [[cobra[0][0], cobra[0][1]]]
        cobra = nova_cobra + cobra[:-1]

        # Preenchimento da janela e desenho da cobra
        janela.fill(PRETO)
        desenhar_cobra(cobra)

        # Atualização da tela
        pygame.display.update()

        # Limitação de FPS
        clock.tick(10)

    pygame.quit()

# Execução do jogo
jogo()
