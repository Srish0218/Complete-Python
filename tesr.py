import numpy as np
import nnfs
from nnfs.datasets import spiral_data

nnfs.init()

X = np.array([[1, 2, 3, 2.5],
              [2, 5, -1, 2],
              [-1.5, 2.7, 3.3, -0.8]])

# Load spiral data
X, Y = spiral_data(100, 3)


class Layer_Dense:
    def __init__(self, n_input, n_neurons):
        self.weights = 0.10 * np.random.randn(n_input, n_neurons)
        self.biases = np.zeros((1, n_neurons))

    def forward(self, inputs):
        self.output = np.dot(inputs, self.weights) + self.biases


class Activation_ReLU:
    def forward(self, inputs):
        self.output = np.maximum(0, inputs)


# Adjust the input layer to match the number of features in the dataset
layer1 = Layer_Dense(2, 5)
activation1 = Activation_ReLU()

# Forward pass
layer1.forward(X)
activation1.forward(layer1.output)

# print(layer1.output)
print(activation1.output)
