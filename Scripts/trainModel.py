import pandas as pd
import tensorflow as tf
import pickle
import os
import numpy as np

def save_model_if_updated(model, pickle_path='model.pkl'):
    # Check if the pickle file exists
    if os.path.exists(pickle_path):
        # Load the previously saved model
        with open(pickle_path, 'rb') as file:
            previous_model = pickle.load(file)
        
        # Compare weights of current model with previous model
        current_weights = model.get_weights()
        previous_weights = previous_model.get_weights()
        
        # If the weights are the same, don't save the model
        if all(np.array_equal(cw, pw) for cw, pw in zip(current_weights, previous_weights)):
            print("Model has not changed. No need to pickle.")
            return
        else:
            print("Model has changed. Saving the updated model.")
    else:
        print("No previous model found. Saving the model.")

    # Save the model (pickle it)
    with open(pickle_path, 'wb') as file:
        pickle.dump(model, file)
    print("Model saved successfully.")



# Load the CSV files
input_data = pd.read_csv('dataset/voltageDataset.csv')
output_data = pd.read_csv('dataset/datasetTrainSigData.csv')

# Convert to numpy arrays
# we need to take the input of the data by columns, 
# hence the transpose needs to be done (otherwise it would take in the training data by rows)
X = input_data.values.T  # Shape: (n_samples, 992)
Y = output_data.values.T  # Shape: (n_samples, 4017)

# Check the shapes of X and Y
print("Input shape:", X.shape)  # Should be (992, 1000) => n_samples = 1000
print("Output shape:", Y.shape)  # Should be (1000, 4017)



# Trainging model
# Define the model
model = tf.keras.Sequential()

# Input layer expecting 992 features
model.add(tf.keras.layers.Input(shape=(992,)))

# Add hidden layers (you can adjust the number of layers and neurons)
# see https://www.kaggle.com/code/dansbecker/rectified-linear-units-relu-in-deep-learning for more details on how it works
model.add(tf.keras.layers.Dense(256, activation='relu'))  # Hidden layer
model.add(tf.keras.layers.Dense(128, activation='relu'))  # Hidden layer

# Output layer with 4017 features
model.add(tf.keras.layers.Dense(4017, activation='sigmoid'))  # Output layer

# Compile the model with mean_squared_error loss and mean_absolute_error as a metric
# formula for Mean_absolute_error
# MSE = (1/n) * sum(Y_o[i] - Y_p[i]) ** 2
# Adam optimizer
# see https://www.geeksforgeeks.org/adam-optimizer/ 
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_absolute_error'])

# Print the model summary to check the structure
model.summary()

# A callback to early stop the epochs when the loss and mean_squared_error is good

# Train the model
# No need to reshape X, it's already in the correct shape
model.fit(X, Y, epochs=50, batch_size=32, validation_split=0.2)  # Adjust epochs and batch size as needed


if __name__ == '__main__':
    save_model_if_updated(model=model)
