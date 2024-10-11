import pandas as pd
import tensorflow as tf

from tensorflow.keras.callbacks import EarlyStopping

# Load the CSV files
input_data = pd.read_csv('dataset/voltageDataset.csv')
output_data = pd.read_csv('dataset/datasetTrainSigData.csv')

# Convert to numpy arrays
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
model.add(tf.keras.layers.Dense(256, activation='relu'))  # Hidden layer
model.add(tf.keras.layers.Dense(128, activation='relu'))  # Hidden layer

# Output layer with 4017 features
model.add(tf.keras.layers.Dense(4017))  # Output layer

# Compile the model with mean_squared_error loss and mean_absolute_error as a metric
model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mean_absolute_error'])

# Print the model summary to check the structure
model.summary()

early_stop = EarlyStopping(monitor='val_mean_absolute_error', patience=10, restore_best_weights=True)

# Train the model
# No need to reshape X, it's already in the correct shape
model.fit(X, Y, epochs=50, batch_size=32, validation_split=0.2, callbacks=[early_stop])  # Adjust epochs and batch size as needed
