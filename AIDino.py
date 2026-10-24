from ai import NeuralNetwork
from dino import Dino


class AIDino:
    def __init__(self, x=110, ground_y=300, scale=1.0):
        self.dino = Dino(x=x, ground_y=ground_y, scale=scale)
        self.dino.load_sprite("pics/dino.png")
        self.nn = NeuralNetwork([3, 6, 1])
        self.alive = True
        self.fitness = 0.0

    def predict(self, inputs):
        return self.nn.predict(inputs)

    def update(self, cactus, dt, screen_width):
        if not self.alive:
            return

        distance = max(0, cactus.x - (self.dino.x + self.dino.width))
        height = max(0, self.dino.ground_y - self.dino.y)
        vertical_speed = max(-1.5, min(1.5, self.dino.ySpeed)) / 1.5
        inputs = [
            min(1.0, distance / screen_width),
            min(1.0, height / 150.0),
            vertical_speed,
        ]
        if self.predict(inputs)[0] > 0.5:
            self.dino.jump()

        self.dino.update(dt)
        if self.dino.collide(cactus):
            self.alive = False
        else:
            self.fitness += dt / 1000.0