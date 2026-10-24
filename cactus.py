import pygame
class Cactus:
    def __init__(self, scale=1.0):
        self.x = 800
        self.scale = scale
        self.width = round(50 * scale)
        self.height = round(85 * scale)
        self.xSpeed = -0.5
        self.sprite = None
        self.currentSprite = "pics/cactus.png"
        self.load_sprite(self.currentSprite)
    
    def draw(self, screen, hitbox=False, y=300):
        screen.blit(self.sprite.image, (self.x, y))
        if hitbox:
            pygame.draw.rect(screen, (0, 160, 0), (self.x, y, self.width, self.height), 1)

    def load_sprite(self, path):
        self.sprite = pygame.sprite.Sprite()
        image = pygame.image.load(path)
        if self.scale != 1.0:
            size = (round(image.get_width() * self.scale), round(image.get_height() * self.scale))
            image = pygame.transform.scale(image, size)
        self.sprite.image = image

    def update(self, dt):
        self.x += self.xSpeed * dt
        if self.x + self.width < 0:
            self.x = 800

    def increase_speed(self, amount):
        self.xSpeed = max(-1.5, self.xSpeed - amount)