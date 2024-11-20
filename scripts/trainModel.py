import argparse

import torch
import torch.nn as nn
import torch.optim as optim
import pandas as pd
import os
import numpy as np

parser = argparse.ArgumentParser(
    prog=__name__,
    description='Trains a model using the csv files in the dataset'
)

parser.add_argument("--input", required=True, help="The input data for voltage data")
parser.add_argument("--output", required=True, help="The output dataset that it is training against")
parser.add_argument("--model_path", default=".model.pth", help="The output of where the model is saved")

args = parser.parse_args()

file_input = args.input
file_output = args.output
model_file = args.model_path


# Check if CUDA is available, otherwise use CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

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


# Load the CSV files
input_data = pd.read_csv(file_input)
output_data = pd.read_csv(file_output)

# Convert to numpy arrays and transpose
X = input_data.values.T  # Shape: (n_samples, 992)
Y = output_data.values.T  # Shape: (n_samples, 4017)

# Convert data to PyTorch tensors
X = torch.tensor(X, dtype=torch.float32).to(device)
Y = torch.tensor(Y, dtype=torch.float32).to(device)

# Check the shapes of X and Y
print("Input shape:", X.shape)  # Should be (992, 1000) => n_samples = 1000
print("Output shape:", Y.shape)  # Should be (1000, 4017)

# Define the model and move it to the appropriate device (CPU or GPU)
model = SimpleModel(input_size=992, hidden_size=256, output_size=4017).to(device)

# Define loss function and optimizer
criterion = nn.MSELoss()  # Mean Squared Error Loss
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Training loop
epochs = 50
batch_size = 32
n_samples = X.shape[0]
validation_split = 0.2
n_val = int(n_samples * validation_split)

# Split into training and validation data
X_train, X_val = X[:n_samples - n_val], X[n_samples - n_val:]
Y_train, Y_val = Y[:n_samples - n_val], Y[n_samples - n_val:]

# Early stopping criterion
best_val_loss = float('inf')

for epoch in range(epochs):
    model.train()
    running_loss = 0.0
    for i in range(0, len(X_train), batch_size):
        inputs = X_train[i:i + batch_size]
        targets = Y_train[i:i + batch_size]

        # Zero the parameter gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(inputs)
        loss = criterion(outputs, targets)

        # Backward pass and optimization
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

    # Validation loss
    model.eval()
    with torch.no_grad():
        val_outputs = model(X_val)
        val_loss = criterion(val_outputs, Y_val)

    print(f"Epoch [{epoch + 1}/{epochs}], Loss: {running_loss / len(X_train)}, Validation Loss: {val_loss.item()}")

torch.save(model.state_dict(), model_file)

