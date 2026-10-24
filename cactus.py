import pygame
class Cactus:
    def __init__(self):
            self.x=800
            self.width = 50
            self.height = 85
            self.xSpeed=-0.5
            self.sprite=None
            self.currentSprite="pics/cactus.png"
            self.load_sprite(self.currentSprite)
    
    def draw(self, screen,hitbox=False):
        screen.blit(self.sprite.image, (self.x, 300))
        if hitbox:
            pygame.draw.rect(screen, (0,255,0), (self.x, 300, self.width, self.height), 2)
    def load_sprite(self, path):
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image=pygame.image.load(path)
    def update(self, dt):
        self.x += self.xSpeed * dt
        if self.x + self.width < 0:
            self.x = 800
    def increase_speed(self, amount):
        self.xSpeed -= amount