import numpy as np
import time
import psutil
import uuid

# Define the data points and classes
data_points = np.array([[1, 0, 1],
                        [0, 1, 1],
                        [1, 1, 0],
                        [0, 0, 1]])

classes = np.array([1, 0, 1, 0])

# Initial weight vector
weights = np.array([-0.5, 1, 0.2])
learning_rate = 1.0

# Function to update weights
def update_weights(weights, data_point, target_class, prediction):
    if prediction != target_class:
        return weights + learning_rate * (target_class - prediction) * data_point
    return weights

# Function to predict class
def predict(weights, data_point):
    return 1 if np.dot(weights, data_point) > 0 else 0

# Initialize
epochs = 0
max_epochs = 100
converged = False

start_time = time.time()

while not converged and epochs < max_epochs:
    converged = True
    for i in range(len(data_points)):
        prediction = predict(weights, data_points[i])
        if prediction != classes[i]:
            converged = False
            weights = update_weights(weights, data_points[i], classes[i], prediction)
    epochs += 1

end_time = time.time()

# Memory consumed
process = psutil.Process()
memory_info = process.memory_info()
memory_consumed = memory_info.rss / (1024 * 1024)  # Convert bytes to MB

# MAC address
def get_mac_address():
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 8)][::-1])
    return mac

# Print results
weight_str = ', '.join(f'{w:.2f}' for w in weights)
print(f"Final weight vector: {weight_str}")
print(f"Epochs run: {epochs}")
print(f"Time consumed: {end_time - start_time:.4f} seconds")
print(f"Memory consumed: {memory_consumed:.2f} MB")
print(f"MAC Address: {get_mac_address()}")

