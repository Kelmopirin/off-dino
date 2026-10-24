class NeuralNetwork:
    def __init__(self, layers):
        self.layers=layers
        self.outputs=[0]*layers[-1]
        self.weights=[]
        for i in range(len(layers)-1):
            self.weights.append([[0]*layers[i] for _ in range(layers[i+1])])
        self.biases=[]
        for i in range(1, len(layers)):
            self.biases.append([0]*layers[i])
        self.learning_rate = 0.01
    
    def sigmoid(self, x):
        import math
        return 1 / (1 + math.exp(-x))

    def sigmoid_derivative(self, x):
        return x * (1 - x)
    def feedforward(self, inputs):
        self.outputs = inputs
        for i in range(len(self.weights)):
            next_outputs = []
            for j in range(len(self.weights[i])):
                activation = sum(self.weights[i][j][k] * self.outputs[k] for k in range(len(self.outputs))) + self.biases[i][j]
                next_outputs.append(self.sigmoid(activation))
            self.outputs = next_outputs
        return self.outputs
    def train(self, inputs, targets):
        outputs = self.feedforward(inputs)
        errors = [targets[i] - outputs[i] for i in range(len(targets))]
        for i in reversed(range(len(self.weights))):
            new_errors = [0]*len(self.weights[i][0])
            for j in range(len(self.weights[i])):
                delta = errors[j] * self.sigmoid_derivative(outputs[j])
                for k in range(len(self.weights[i][j])):
                    new_errors[k] += self.weights[i][j][k] * delta
                    self.weights[i][j][k] += self.learning_rate * delta * (self.outputs[k] if i == 0 else self.outputs[k])
                self.biases[i][j] += self.learning_rate * delta
            errors = new_errors
    def predict(self, inputs):
        return self.feedforward(inputs)
    
    