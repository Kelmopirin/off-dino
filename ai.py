import math
import random


class NeuralNetwork:
    def __init__(self, layers):
        if len(layers) < 2 or any(size <= 0 for size in layers):
            raise ValueError("A hálónak legalább két pozitív méretű rétegre van szüksége.")

        self.layers = list(layers)
        self.weights = [
            [
                [random.uniform(-1.0, 1.0) for _ in range(input_size)]
                for _ in range(output_size)
            ]
            for input_size, output_size in zip(self.layers, self.layers[1:])
        ]
        self.biases = [
            [random.uniform(-1.0, 1.0) for _ in range(size)]
            for size in self.layers[1:]
        ]

    @staticmethod
    def sigmoid(value):
        value = max(-60.0, min(60.0, value))
        return 1.0 / (1.0 + math.exp(-value))

    def feedforward(self, inputs):
        if len(inputs) != self.layers[0]:
            raise ValueError(
                f"A háló {self.layers[0]} bemenetet vár, de {len(inputs)} érkezett."
            )

        outputs = list(inputs)
        for layer_weights, layer_biases in zip(self.weights, self.biases):
            outputs = [
                self.sigmoid(
                    sum(weight * value for weight, value in zip(neuron_weights, outputs))
                    + bias
                )
                for neuron_weights, bias in zip(layer_weights, layer_biases)
            ]
        return outputs

    def predict(self, inputs):
        return self.feedforward(inputs)

    def clone(self):
        clone = NeuralNetwork(self.layers)
        clone.weights = [
            [list(neuron_weights) for neuron_weights in layer]
            for layer in self.weights
        ]
        clone.biases = [list(layer) for layer in self.biases]
        return clone

    def crossover(self, other, mutation_rate=0.1, mutation_strength=0.5):
        if self.layers != other.layers:
            raise ValueError("Csak azonos felépítésű hálók keresztezhetők.")

        child = NeuralNetwork(self.layers)

        def inherit(gene_a, gene_b):
            gene = random.choice((gene_a, gene_b))
            if random.random() < mutation_rate:
                gene += random.gauss(0.0, mutation_strength)
            return gene

        child.weights = [
            [
                [
                    inherit(weight_a, weight_b)
                    for weight_a, weight_b in zip(neuron_a, neuron_b)
                ]
                for neuron_a, neuron_b in zip(layer_a, layer_b)
            ]
            for layer_a, layer_b in zip(self.weights, other.weights)
        ]
        child.biases = [
            [
                inherit(bias_a, bias_b)
                for bias_a, bias_b in zip(layer_a, layer_b)
            ]
            for layer_a, layer_b in zip(self.biases, other.biases)
        ]
        return child
