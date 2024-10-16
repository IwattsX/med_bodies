import dill as pickle
import os
import pandas as pd
import torch
from scipy.io import savemat

from trainModel import SimpleModel  # Make sure trainModel is available and SimpleModel is defined

# Check if CUDA is available, otherwise use CPU
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def load_pickled_model(pickle_path='model.pkl'):
    if os.path.exists(pickle_path):
        with open(pickle_path, 'rb') as file:
            model = pickle.load(file)
        print("Model loaded successfully.")
        return model
    else:
        print("No pickled model found.")
        return None


# Load the model
model = load_pickled_model()

# If model is not None, move it to the appropriate device and set it to evaluation mode
if model is not None:
    model = model.to(device)
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
if model is not None:
    with torch.no_grad():  # Ensure no gradients are calculated during prediction
        predictions = model(X_tensor)  # Forward pass
        predictions = predictions.cpu().numpy()  # Move the predictions back to the CPU and convert to numpy

    # Save the prediction for the i-th column into a .mat file
    savemat(f"prediction_column_{i}.mat", {'predicted_output': predictions[i]})
    print(f"Prediction for column {i} saved to prediction_column_{i}.mat")
