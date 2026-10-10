import pygame
from dino import Dino
width, heigth=800,600
screen = pygame.display.set_mode((width,heigth))

dino=Dino()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((255,255,255))
    dino.draw(screen)
    pygame.display.flip()

pygame.quit()