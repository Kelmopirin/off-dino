import random

from bird import Bird
from cactus import Cactus


class ObstacleCourse:
    """Véletlenszerűen választ kaktusz, magas madár és alacsony madár között."""

    def __init__(self, screen_width, dino_scale, cactus_scale):
        self.screen_width = screen_width
        self.speed = -0.5
        self.max_speed = -1.5
        self.pool = [
            (Cactus(scale=cactus_scale), 0.45),
            (Bird("high", scale=dino_scale), 0.30),
            (Bird("low", scale=dino_scale), 0.25),
        ]
        self.current = self.pool[0][0]
        self.reset()

    def _spawn(self, extra_gap=0):
        obstacles, weights = zip(*self.pool)
        self.current = random.choices(obstacles, weights=weights)[0]
        self.current.x = self.screen_width + extra_gap

    def reset(self):
        self._spawn(random.randint(0, 150))

    def update(self, dt):
        self.current.update(dt, self.speed)
        if self.current.x + self.current.width < 0:
            self._spawn(random.randint(0, 250))

    def increase_speed(self, amount):
        self.speed = max(self.max_speed, self.speed - amount)
