class Dino:
    def __init__(self):
        self.y = 300
        self.width = 50
        self.height = 50
        self.color = (0, 255, 0)
        self.ySpeed=0

    def draw(self, screen):
        import pygame
        pygame.draw.rect(screen, self.color, (800*0.2, self.y, self.width, self.height))
    def jump(self):
        self.ySpeed=-3
    def update(self):
        self.y+=self.ySpeed
        self.ySpeed+=0.1
        if self.y>=300:
            self.y=300
            self.ySpeed=0
