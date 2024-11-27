import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.layers import Input
import numpy as np
import time
import psutil
import uuid
import platform
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

def get_mac_address():
    # Get MAC address
    if platform.system() == 'Windows':
        return ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 8)][::-1])
    else:
        return ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 8)][::-1])

def build_model(num_layers):
    model = Sequential()
    model.add(Input(shape=(2,)))  # Specify input shape using Input layer
    model.add(Dense(8, activation='relu'))  # First hidden layer
    for _ in range(num_layers):
        model.add(Dense(8, activation='relu'))  # Additional hidden layers
    model.add(Dense(1, activation='sigmoid'))  # Output layer
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def main():
    # Display MAC address
    mac_address = get_mac_address()
    print(f"MAC Address: {mac_address}")
    
    # Generate synthetic data
    X = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y = np.array([[0], [0], [1], [0]])  # x1 > x2
    
    # User specifies the number of layers
    num_layers = int(input("Enter the number of hidden layers: "))
    
    # Build the model
    model = build_model(num_layers)
    
    # Measure time taken for training
    start_time = time.time()
    
    # Train the model
    model.fit(X, y, epochs=1000, verbose=0)
    
    elapsed_time = time.time() - start_time
    
    # Display the time taken
    print(f"Time taken for training: {elapsed_time:.2f} seconds")
    
    # Display the memory consumed
    process = psutil.Process()
    memory_info = process.memory_info()
    print(f"Memory consumed: {memory_info.rss / (1024 * 1024):.2f} MB")

    # Test the model
    predictions = model.predict(X)
    print("\nPredictions:")
    for i, pred in enumerate(predictions):
        print(f"Input: {X[i]} - Prediction: {pred[0]:.2f} - Expected: {y[i][0]}")

if __name__ == "__main__":
    main()

