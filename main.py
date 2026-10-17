import pygame
from dino import Dino
from cactus import Cactus
width, heigth=800,600
screen = pygame.display.set_mode((width,heigth))

dino=Dino()
cactus=Cactus()

dino.load_sprite("pics/dino.png")
running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                dino.jump()
    screen.fill((255,255,255))
    dino.draw(screen)
    cactus.draw(screen)
    pygame.display.flip()
    dt = clock.tick(60)
    dino.update(dt)


pygame.quit()
