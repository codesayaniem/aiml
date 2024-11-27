import numpy as np
import matplotlib.pyplot as plt
import psutil
import time
import uuid

def get_mac_address():
    mac = hex(uuid.getnode()).replace('0x', '').upper()
    return ':'.join(mac[i:i+2] for i in range(0, len(mac), 2))

def convolution2d(input_matrix, kernel, stride):
    kernel_height, kernel_width = kernel.shape
    input_height, input_width = input_matrix.shape
    output_height = (input_height - kernel_height) // stride + 1
    output_width = (input_width - kernel_width) // stride + 1
    output = np.zeros((output_height, output_width))
    
    for y in range(output_height):
        for x in range(output_width):
            output[y, x] = np.sum(
                input_matrix[y*stride:y*stride + kernel_height, x*stride:x*stride + kernel_width] * kernel
            )
    
    return output

def pooling(feature_map, pool_size, mode='max'):
    height, width = feature_map.shape
    pooled_height = height // pool_size
    pooled_width = width // pool_size
    pooled = np.zeros((pooled_height, pooled_width))
    
    for y in range(pooled_height):
        for x in range(pooled_width):
            region = feature_map[y*pool_size:(y+1)*pool_size, x*pool_size:(x+1)*pool_size]
            if mode == 'max':
                pooled[y, x] = np.max(region)
            elif mode == 'average':
                pooled[y, x] = np.mean(region)
            elif mode == 'sum':
                pooled[y, x] = np.sum(region)
    
    return pooled

def visualize_flattened(feature_maps):
    flattened = feature_maps.flatten()
    plt.figure(figsize=(10, 5))
    plt.bar(range(len(flattened)), flattened)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Flattened Pooled Feature Maps')
    plt.show()
    return flattened

def learn_weights(flattened_data, epochs=1):
    weights = np.random.rand(flattened_data.shape[0])
    bias = 1
    learning_rate = 0.01

    for _ in range(epochs):
        predictions = np.dot(flattened_data, weights) + bias
        error = predictions - flattened_data  # Sample target is the same as input for simplicity
        weights -= learning_rate * np.dot(flattened_data, error) / len(flattened_data)
        bias -= learning_rate * np.mean(error)
    
    return weights, bias

# Main Function
def main():
    # Get MAC address
    mac_address = get_mac_address()
    print(f"MAC Address: {mac_address}")

    # Input matrix and kernel
    print("Enter a 5x5 input matrix (25 space-separated values):")
    input_matrix = np.array([[int(x) for x in input().split()] for _ in range(5)])
    
    print("Enter a 3x3 kernel matrix (9 space-separated values):")
    kernel = np.array([[int(x) for x in input().split()] for _ in range(3)])

    # Measure memory and time before processing
    mem_before = psutil.virtual_memory().used
    start_time = time.time()

    # Convolution with stride 1 and 2
    conv1 = convolution2d(input_matrix, kernel, stride=1)
    conv2 = convolution2d(input_matrix, kernel, stride=2)

    print(f"Convolution output (stride=1):\n{conv1}")
    print(f"Convolution output (stride=2):\n{conv2}")

    # Pooling
    pooled_max = pooling(conv1, pool_size=2, mode='max')
    pooled_average = pooling(conv1, pool_size=2, mode='average')
    pooled_sum = pooling(conv1, pool_size=2, mode='sum')

    print(f"Max Pooling:\n{pooled_max}")
    print(f"Average Pooling:\n{pooled_average}")
    print(f"Sum Pooling:\n{pooled_sum}")

    # Visualization
    flattened = visualize_flattened(pooled_max)

    # Learning weights and bias
    weights, bias = learn_weights(flattened, epochs=1)
    print(f"Learned Weights:\n{weights}")
    print(f"Learned Bias:\n{bias}")

    # Measure memory and time after processing
    mem_after = psutil.virtual_memory().used
    time_taken = time.time() - start_time

    # Output memory consumed and time taken
    print(f"Memory consumed: {mem_after - mem_before} bytes")
    print(f"Time taken: {time_taken:.4f} seconds")

if __name__ == "__main__":
    main()

