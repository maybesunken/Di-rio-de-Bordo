import pygame

WIDTH = 1920
HEIGHT = 1080
FPS = 90

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Andando com seu personagem")
clock = pygame.time.Clock()
imagesdireita = [pygame.image.load("andar.png"), pygame.image.load("andar2.png")]
imagesesquerda = [pygame.image.load("andaresquerda.png"), pygame.image.load("andar2esquerda.png")]
imagespulo = [pygame.image.load("pular.png")]
imagespulo2 = [pygame.image.load("pular2.png")]
imagespulo2_index = 0
imagepulo_index = 0
pulo_transition = 0
pulo_transition_speed = 5  # Ajuste a velocidade do pulo duplo aqui
second_jump_transition = 0
second_jump_transition_speed = 10  # Ajuste a velocidade da transição do segundo pulo aqui
image_change_delay = 500  # Ajuste o atraso entre as mudanças de imagem em milissegundos

xpos = 0
ypos = 100
deltaX = 0
deltaY = 0
indexImg = 0
pressionado = 0
jumping = False
jump_count = 8
gravity = 0.8
max_jumps = 2

remaining_jumps = max_jumps
second_jump_available = False

background_image = pygame.image.load("fundo.jpg")

running = True
last_image_change_time = pygame.time.get_ticks()  # Registra o tempo da última mudança de imagem

while running:
    current_time = pygame.time.get_ticks()  # Obtém o tempo atual do jogo

    for event in pygame.event.get():
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                deltaX = 0
            if event.key == pygame.K_RIGHT:
                deltaX = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                deltaX = -5
                pressionado = 1
            if event.key == pygame.K_RIGHT:
                deltaX = 5
                pressionado = 2
            if event.key == pygame.K_SPACE and remaining_jumps > 0:
                jumping = True
                deltaY = -jump_count
                remaining_jumps -= 1
                second_jump_available = True
                imagepulo_index = 0
                pulo_transition = 0
            if event.key == pygame.K_SPACE and remaining_jumps == 0 and second_jump_available:
                jumping = True
                deltaY = -jump_count
                second_jump_transition = 0
                second_jump_available = False
                imagespulo2_index = 0  # Reinicia o índice da segunda imagem do pulo

        if event.type == pygame.QUIT:
            running = False

    if jumping:
        deltaY += gravity
        ypos += deltaY
        if ypos >= 100:
            ypos = 100
            jumping = False
            remaining_jumps = max_jumps

    xpos += deltaX
    if deltaX != 0:
        indexImg = (indexImg + 1) % 2

    if xpos < -25:
        xpos = WIDTH - 1
    elif xpos > WIDTH:
        xpos = 0

    screen.blit(background_image, (0, 0))

    # Verifica se é hora de mudar para a próxima imagem de pulo
    if current_time - last_image_change_time >= image_change_delay:
        if imagepulo_index < len(imagespulo):
            screen.blit(imagespulo[imagepulo_index], (xpos, ypos))
            imagepulo_index += 1
            last_image_change_time = current_time  # Atualiza o tempo da última mudança de imagem

        # Verifica se é hora de mudar para a próxima imagem do segundo pulo
        if imagespulo2_index < len(imagespulo2):
            imagespulo2_surface = imagespulo2[imagespulo2_index]
            imagespulo2_surface.set_alpha(min(255, second_jump_transition))
            screen.blit(imagespulo2_surface, (xpos, ypos))
            imagespulo2_index += 1
            second_jump_transition += second_jump_transition_speed

    elif deltaX > 0:
        screen.blit(imagesdireita[indexImg], (xpos, ypos))
    elif deltaX < 0:
        screen.blit(imagesesquerda[indexImg], (xpos, ypos))
    elif deltaX == 0 and pressionado == 1:
        screen.blit(imagesesquerda[1], (xpos, ypos))  # Mudança aqui
    elif deltaX == 0 and pressionado == 2:
        screen.blit(imagesdireita[1], (xpos, ypos))  # Mudança aqui

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
