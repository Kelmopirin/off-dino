import pygame
class Dino:
    def __init__(self):
        self.y = 300
        self.width = 80
        self.height = 70
        self.ySpeed=0
        self.sprite=None
        self.animationTime=300
        self.currentTime=0
        self.currentSprite="pics/dino.png"
        self.collision=False

    def draw(self, screen, hitbox=False):
            screen.blit(self.sprite.image, (800*0.2, self.y))
            if hitbox:
                if self.collision:
                    pygame.draw.rect(screen, (255,0,0), (800*0.2, self.y, self.width, self.height), 2)
                else:
                    pygame.draw.rect(screen, (0,255,0), (800*0.2, self.y, self.width, self.height), 2)

    def jump(self):
        if self.y==300:
            self.ySpeed=-1
    def update(self,dt):
        self.y+=self.ySpeed*dt
        self.ySpeed+=0.003*dt
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
    def collide(self, cactus):
        dino_rect = pygame.Rect(800*0.2, self.y, self.width, self.height)
        cactus_rect = pygame.Rect(cactus.x, 300, cactus.width, cactus.height)
        self.collision = dino_rect.colliderect(cactus_rect)
    
