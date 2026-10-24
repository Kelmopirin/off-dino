from ai import NeuralNetwork
from dino import Dino
class AIDino:
    def __init__(self):
        self.dino = Dino()
        self.nn = NeuralNetwork([0,0,0])
    
    def train(self, inputs, targets):
        self.nn.train(inputs, targets)

    def predict(self, inputs):
        return self.nn.predict(inputs)
    def set_inputs(self, inputs):
        self.nn.layers[0] = inputs