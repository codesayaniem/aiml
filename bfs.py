import psutil
import time
import uuid
from collections import deque

# Define the graph as an adjacency list
graph = {
    'B': ['E', 'X', 'K'],
    'E': ['P'],
    'X': [],
    'K': ['A'],
    'P': ['D', 'T'],
    'G': ['M'],
    'A': ['R', 'G'],
    'R': [],
    'D': [],
    'T': [],
    'H': [],
    'M': []
}

# Function for BFS
def bfs(graph, start_node, end_node):
    visited = set()
    queue = deque([[start_node]])

    if start_node == end_node:
        return [start_node]

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node not in visited:
            neighbors = graph[node]
            for neighbor in neighbors:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)

                if neighbor == end_node:
                    return new_path

            visited.add(node)

    return None

# Get MAC address
def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0, 12, 2)])

# Measure memory usage
def get_memory_usage():
    process = psutil.Process()
    mem_info = process.memory_info()
    return mem_info.rss / (1024 ** 2)  # Convert bytes to MB

# Measure time taken
start_time = time.time()
path = bfs(graph, 'B', 'M')
end_time = time.time()

# Print results
if path:
    print("Path from B to M:", " -> ".join(path))
else:
    print("No path found from B to M")

print("MAC Address:", get_mac_address())
print("Memory Consumed: {:.2f} MB".format(get_memory_usage()))
print("Time Consumed: {:.6f} seconds".format(end_time - start_time))

