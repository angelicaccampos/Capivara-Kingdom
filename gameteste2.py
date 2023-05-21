import pygame

# Inicialização do Pygame
pygame.init()

# Definição das cores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 165, 0)

# Definição da largura e altura da tela
screen_width = 800
screen_height = 600

# Criação da tela
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Personagem Andando")

# Carregamento das imagens
image1 = pygame.image.load("image1.png")
image2 = pygame.image.load("image2.png")

# Definição inicial da imagem atual do personagem
character_image = image1

# Posição inicial do personagem
character_rect = character_image.get_rect()
character_rect.centerx = screen_width // 2
character_rect.bottom = screen_height - 10

# Velocidade de movimento do personagem
character_speed = 5

# Controle para alternar entre as imagens
image_index = 0

# Variável para controlar o flip horizontal
flip = False

# Loop principal do jogo
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Verificação das teclas pressionadas
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        character_rect.x -= character_speed
        flip = False
        image_index += 1
    if keys[pygame.K_RIGHT]:
        character_rect.x += character_speed
        flip = True
        image_index += 1
    if keys[pygame.K_UP]:
        character_rect.y -= character_speed
        image_index += 1
    if keys[pygame.K_DOWN]:
        character_rect.y += character_speed
        image_index += 1

    # Alterna entre as imagens do personagem
    if image_index % 2 == 0:
        character_image = image1
    else:
        character_image = image2

    # Limpeza da tela
    screen.fill(WHITE)

    # Desenho do personagem na tela
    if flip:
        character_image_flipped = pygame.transform.flip(character_image, True, False)
        screen.blit(character_image_flipped, character_rect)
    else:
        screen.blit(character_image, character_rect)

    # Atualização da tela
    pygame.display.flip()

    # Aguarda um curto intervalo de tempo para reduzir a velocidade de alternância das imagens
    pygame.time.delay(100)

# Encerramento do Pygame
pygame.quit()
