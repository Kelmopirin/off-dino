import pygame
class Dino:
    def __init__(self):
        self.y = 300
        self.width = 50
        self.height = 50
        self.color = (0, 255, 0)
        self.ySpeed=0
        self.sprite=None

    def draw(self, screen):
            screen.blit(self.sprite.image, (800*0.2, self.y))
    def jump(self):
        self.ySpeed=-2
    def update(self,dt):
        self.y+=self.ySpeed*dt
        self.ySpeed+=0.01*dt
        if self.y>=300:
            self.y=300
            self.ySpeed=0
    def load_sprite(self, path):
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image=pygame.image.load(path)
