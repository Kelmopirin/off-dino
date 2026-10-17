import pygame
class Dino:
    def __init__(self):
        self.y = 300
        self.width = 80
        self.height = 80
        self.ySpeed=0
        self.sprite=None
        self.animationTime=300
        self.currentTime=0
        self.currentSprite="pics/dino.png"

    def draw(self, screen, hitbox=False):
            screen.blit(self.sprite.image, (800*0.2, self.y))
            if hitbox:
                pygame.draw.rect(screen, (255, 0, 0), (800*0.2, self.y, self.width, self.height), 2)
    def jump(self):
        if self.y==300:
            self.ySpeed=-2
    def update(self,dt):
        self.y+=self.ySpeed*dt
        self.ySpeed+=0.01*dt
        if self.y>=300:
            self.y=300
            self.ySpeed=0
        self.currentTime+=dt
        if self.currentTime >= self.animationTime:
            self.currentTime = 0
            if self.currentSprite=="pics/dino.png":
                self.currentSprite="pics/dino1.png"
                self.load_sprite(self.currentSprite)
            elif self.currentSprite=="pics/dino1.png":
                self.currentSprite="pics/dino.png"
                self.load_sprite(self.currentSprite)
    def load_sprite(self, path):
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image=pygame.image.load(path)
    
