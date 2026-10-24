import pygame
class Dino:
    def __init__(self, x=160, ground_y=300, scale=1.0):
        self.x = x
        self.ground_y = ground_y
        self.scale = scale
        self.y = ground_y
        self.width = round(80 * scale)
        self.height = round(70 * scale)
        self.ySpeed = 0
        self.sprite=None
        self.animationTime=300
        self.currentTime=0
        self.currentSprite="pics/dino.png"
        self.collision=False

    def draw(self, screen, hitbox=False):
        screen.blit(self.sprite.image, (self.x, self.y))
        if hitbox:
            color = (255, 0, 0) if self.collision else (0, 160, 0)
            pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height), 1)

    def jump(self):
        if self.y >= self.ground_y:
            self.ySpeed = -1

    def update(self, dt):
        self.y += self.ySpeed * dt
        self.ySpeed += 0.003 * dt
        if self.y >= self.ground_y:
            self.y = self.ground_y
            self.ySpeed = 0
        self.currentTime += dt
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
        image = pygame.image.load(path)
        if self.scale != 1.0:
            size = (round(image.get_width() * self.scale), round(image.get_height() * self.scale))
            image = pygame.transform.scale(image, size)
        self.sprite.image = image

    def collide(self, cactus, cactus_y=None):
        if cactus_y is None:
            cactus_y = self.ground_y
        dino_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        cactus_rect = pygame.Rect(cactus.x, cactus_y, cactus.width, cactus.height)
        self.collision = dino_rect.colliderect(cactus_rect)
        return self.collision
    
