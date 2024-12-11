import argparse
import os
import pandas as pd
import torch
from scipy.io import savemat

from NNModel import SimpleModel

# Argument parser
parser = argparse.ArgumentParser(
    prog=__name__,
    description='Puts the model into prediction mode'
)
parser.add_argument("--input", required=True, help="The input data for voltage data .csv")
parser.add_argument("--output", required=True, help="The output dataset that contains predictions .mat")
parser.add_argument("--model", required=True, help="Path to the trained model file (.pth)")

args = parser.parse_args()

input_file = args.input
output_file = args.output

# Validate input file
if not os.path.isfile(input_file):
    raise FileNotFoundError(f"Input file '{input_file}' not found.")
    
# Validate model file
if not os.path.isfile(args.model):
    raise FileNotFoundError(f"Model file '{args.model}' not found.")

# Create output directory if needed
output_dir = os.path.dirname(output_file)
if output_dir and not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Device setup
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

# Load the model
model = SimpleModel(input_size=992, hidden_size=256, output_size=1029)
model.load_state_dict(torch.load(args.model, map_location=device))
model.to(device)
model.eval()

# Load the dataset
input_data = pd.read_csv(input_file)

# Convert to tensor
X = input_data.values.T  # Transpose if necessary
X_tensor = torch.tensor(X, dtype=torch.float32).to(device)

# Prediction
with torch.no_grad():
    predictions = model(X_tensor).cpu().numpy()

# Save predictions
savemat(output_file, {'predicted_output': predictions})
print(f"Predictions saved to {output_file}")
