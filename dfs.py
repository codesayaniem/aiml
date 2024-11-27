import time
import psutil
import uuid

# Define the graph as an adjacency list
graph = {
    '1': ['2', '7'],
    '2': ['3', '6'],
    '3': ['4'],
    '4': [],
    '5': [],
    '6': ['5'],
    '7': ['8'],
    '8': ['9'],
    '9': ['10', '12'],
    '10': ['11'],
    '11': [],
    '12': []
}

# DFS function
def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')
    
    for next_node in graph[start]:
        if next_node not in visited:
            dfs(graph, next_node, visited)

# Function to get MAC address
def get_mac_address():
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> ele) & 0xff) for ele in range(0, 8*6, 8)][::-1])
    return mac

# Function to get memory usage
def get_memory_usage():
    process = psutil.Process()
    mem_info = process.memory_info()
    return mem_info.rss

# Main function to perform DFS and print system info
def main():
    start_time = time.process_time()
    
    print("DFS starting from node 1:")
    dfs(graph, '1')
    print("\n")
    
    print("DFS starting from node 7:")
    dfs(graph, '7')
    print("\n")
    
    end_time = time.process_time()
    elapsed_time = end_time - start_time
    
    mac_address = get_mac_address()
    memory_usage = get_memory_usage()
    
    print(f"MAC Address: {mac_address}")
    print(f"Memory Consumed: {memory_usage} bytes")
    print(f"Time Consumed: {elapsed_time} seconds")

if __name__ == "__main__":
    main()

