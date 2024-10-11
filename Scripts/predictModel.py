import pickle
import os
import pandas as pd
from scipy.io import savemat

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

# Load the dataset
input_data = pd.read_csv('dataset/voltageDataset.csv')

# Transpose the data (if needed, you can remove the transpose if your data is already organized by columns)
X = input_data.values.T

# Specify the index of the column you want to inspect (adjust i to your desired column number)
i = 0  # Example: Get the 5th column (you can set it to any column index you want)

# Print the i-th column for testing in MATLAB
print(f"Column {i}: {X[:, i]}")

# Make a prediction using the model on the entire dataset
if model is not None:
    predictions = model.predict(X)

    # Save the prediction for the i-th column into a .mat file
    savemat(f"prediction_column_{i}.mat", {'predicted_output': predictions[i]})
    print(f"Prediction for column {i} saved to prediction_column_{i}.mat")

