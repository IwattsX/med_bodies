import os
import pandas as pd
import torch
from scipy.io import savemat

from trainModel import SimpleModel  # Ensure trainModel is available and SimpleModel is defined

# Check if CUDA is available, otherwise use CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the model
model = SimpleModel(input_size=992, hidden_size=256, output_size=4017)
model.load_state_dict(torch.load("model.pth", map_location=device))  # Corrected this line to properly load the state dict

# Move the model to the appropriate device
model.to(device)

# Set the model to evaluation mode
model.eval()

# Load the dataset
input_data = pd.read_csv('dataset/voltageDataset.csv')

# Transpose the data (if needed, you can remove the transpose if your data is already organized by columns)
X = input_data.values.T

# Convert the input data to a PyTorch tensor and move it to the correct device
X_tensor = torch.tensor(X, dtype=torch.float32).to(device)

# Specify the index of the column you want to inspect (adjust i to your desired column number)
i = 0  # Example: Get the 1st column (you can set it to any column index you want)

# Print the i-th column for testing
print(f"Column {i}: {X[:, i]}")

# Make a prediction using the model on the entire dataset
with torch.no_grad():  # Ensure no gradients are calculated during prediction
    predictions = model(X_tensor)  # Forward pass
    predictions = predictions.cpu().numpy()  # Move the predictions back to the CPU and convert to numpy

# Save the prediction for the i-th column into a .mat file
savemat(f"prediction_column_{i}.mat", {'predicted_output': predictions[i]})
print(f"Prediction for column {i} saved to prediction_column_{i}.mat")
