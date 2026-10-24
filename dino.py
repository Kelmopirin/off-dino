import pygame
class Dino:
    def __init__(self, x=160, ground_y=300, scale=1.0):
        self.x = x
        self.ground_y = ground_y
        self.scale = scale
        self.y = ground_y
        self.width = round(80 * scale)
        self.height = round(70 * scale)
        self.duck_height = round(31 * scale)
        self.duck_width = round(110 * scale)
        self.ducking = False
        self.duck_sprite = None
        self.ySpeed = 0
        self.sprite=None
        self.animationTime=300
        self.currentTime=0
        self.currentSprite="pics/dino.png"
        self.collision=False

    def draw(self, screen, hitbox=False):
        image = self.sprite.image
        if self.is_ducking:
            duck_image = self.duck_sprite.image
            screen.blit(duck_image, (self.x, self.y + image.get_height() - duck_image.get_height()))
        else:
            screen.blit(image, (self.x, self.y))
        if hitbox:
            color = (255, 0, 0) if self.collision else (0, 160, 0)
            pygame.draw.rect(screen, color, self.rect, 1)

    @property
    def is_ducking(self):
        return self.ducking and self.y >= self.ground_y

    @property
    def rect(self):
        if self.is_ducking:
            return pygame.Rect(self.x, self.y + self.height - self.duck_height, self.duck_width, self.duck_height)
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def jump(self):
        if self.y >= self.ground_y:
            self.ySpeed = -1

    def duck(self, active=True):
        self.ducking = active

    def update(self, dt):
        self.y += self.ySpeed * dt
        # Levegőben a gugolás gyorsított zuhanás.
        gravity = 0.009 if self.ducking and self.y < self.ground_y else 0.003
        self.ySpeed += gravity * dt
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

    def _load_image(self, path):
        image = pygame.image.load(path)
        if self.scale != 1.0:
            size = (round(image.get_width() * self.scale), round(image.get_height() * self.scale))
            image = pygame.transform.scale(image, size)
        return image

    def load_sprite(self, path):
        self.sprite = pygame.sprite.Sprite()
        self.sprite.image = self._load_image(path)

    def load_duck_sprite(self, path):
        self.duck_sprite = pygame.sprite.Sprite()
        self.duck_sprite.image = self._load_image(path)

    def collide(self, obstacle):
        obstacle_rect = pygame.Rect(
            obstacle.x, self.ground_y + obstacle.y_offset, obstacle.width, obstacle.height
        )
        self.collision = self.rect.colliderect(obstacle_rect)
        return self.collision
    
