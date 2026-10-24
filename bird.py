import pygame


class Bird:
    """Repülő akadály: 'high' alatt le lehet gugolni, 'low' fölött ugrani kell."""

    def __init__(self, variant="high", scale=1.0):
        self.variant = variant
        self.x = 800
        self.width = round(80 * scale)
        self.height = round(36 * scale)
        self.y_offset = 0 if variant == "high" else round(40 * scale)
        self.speed_factor = 1.2
        image = pygame.image.load("pics/Pterodactyl.png")
        factor = 0.46 * scale
        size = (round(image.get_width() * factor), round(image.get_height() * factor))
        self.image = pygame.transform.scale(image, size)

    def draw(self, screen, hitbox=False, y=300):
        top = y + self.y_offset
        screen.blit(
            self.image,
            (
                self.x - (self.image.get_width() - self.width) // 2,
                top - (self.image.get_height() - self.height) // 2,
            ),
        )
        if hitbox:
            pygame.draw.rect(screen, (0, 160, 0), (self.x, top, self.width, self.height), 1)

    def update(self, dt, speed):
        self.x += speed * self.speed_factor * dt
