import torch
import torch.nn as nn
import torch.optim as optim

class SimpleModel(nn.Module):
    def __init__(self, input_size, hidden_size, output_size):
        super(SimpleModel, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)  # Input to hidden layer
        self.elu = nn.ELU()  # Activation function
        self.fc2 = nn.Linear(hidden_size, output_size)  # Hidden to output layer
        self.sigmoid = nn.Sigmoid()  # Activation for output layer

    def forward(self, x):
        x = self.fc1(x)
        x = self.elu(x)
        x = self.fc2(x)
        x = self.sigmoid(x)
        return x