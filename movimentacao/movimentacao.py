import pygame

WIDTH = 800
HEIGHT = 380
FPS = 90
GRAY = (128, 128, 128)

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Andando com seu personagem")
clock = pygame.time.Clock()
imagesdireita = [pygame.image.load("andar.png"), pygame.image.load("andar2.png")]
imagesesquerda = [pygame.image.load("andaresquerda.png"), pygame.image.load("andar2esquerda.png")]
imagespulo = [pygame.image.load("pular.png"), pygame.image.load("pular2.png")]
imagepulo_index = 0  # Defina a variável imagepulo_index aqui

xpos = 0
ypos = 100
deltaX = 0
deltaY = 0
indexImg = 0
pressionado = 0
jumping = False
jump_count = 10
gravity = 1
max_jumps = 2

remaining_jumps = max_jumps
second_jump_available = False

running = True
while running:
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
                second_jump_available = False
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

    screen.fill(GRAY)
    if jumping:
        screen.blit(imagespulo[imagepulo_index], (xpos, ypos))
        imagepulo_index = (imagepulo_index + 1) % len(imagespulo)
    elif deltaX > 0:
        screen.blit(imagesdireita[indexImg], (xpos, ypos))
    elif deltaX < 0:
        screen.blit(imagesesquerda[indexImg], (xpos, ypos))
    elif deltaX == 0 and pressionado == 1:
        screen.blit(imagesesquerda[0], (xpos, ypos))
    elif deltaX == 0 and pressionado == 2:
        screen.blit(imagesdireita[0], (xpos, ypos))
    pygame.display.flip()
    clock.tick(60)

pygame.quit()