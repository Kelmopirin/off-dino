import pygame
class Cactus:
    def __init__(self, scale=1.0):
        self.x = 800
        self.scale = scale
        self.width = round(50 * scale)
        self.height = round(85 * scale)
        self.y_offset = 0
        self.speed_factor = 1.0
        self.sprite = None
        self.currentSprite = "pics/cactus.png"
        self.load_sprite(self.currentSprite)
    
    def draw(self, screen, hitbox=False, y=300):
        screen.blit(self.sprite.image, (self.x, y + self.y_offset))
        if hitbox:
            pygame.draw.rect(screen, (0, 160, 0), (self.x, y + self.y_offset, self.width, self.height), 1)

    def load_sprite(self, path):
        self.sprite = pygame.sprite.Sprite()
        image = pygame.image.load(path)
        if self.scale != 1.0:
            size = (round(image.get_width() * self.scale), round(image.get_height() * self.scale))
            image = pygame.transform.scale(image, size)
        self.sprite.image = image

    def update(self, dt, speed):
        self.x += speed * self.speed_factor * dt