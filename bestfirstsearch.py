import heapq
import time
import psutil
import uuid

def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0, 11, 2)])

def greedy_best_first_search(graph, start_node, stop_node):
    visited = set()
    priority_queue = [(graph[start_node]['heuristic'], start_node)]
    path = []
    
    while priority_queue:
        current_heuristic_cost, current_node = heapq.heappop(priority_queue)
        path.append(current_node)
        if current_node == stop_node:
            return path
        visited.add(current_node)
        
        for neighbor in graph[current_node]['neighbors']:
            if neighbor not in visited:
                heapq.heappush(priority_queue,
                               (graph[neighbor]['heuristic'], neighbor))
    return []

# Define graph with heuristic costs
graph = {
    'Src': {'heuristic': 20, 'neighbors': ['1', '2', '3']},
    '1': {'heuristic': 22, 'neighbors': ['4']},
    '2': {'heuristic': 21, 'neighbors': ['5', '6']},
    '3': {'heuristic': 10, 'neighbors': ['7', '8']},
    '4': {'heuristic': 25, 'neighbors': ['dest']},
    '5': {'heuristic': 24, 'neighbors': ['dest']},
    '6': {'heuristic': 30, 'neighbors': ['dest']},
    '7': {'heuristic': 5, 'neighbors': ['dest']},
    '8': {'heuristic': 12, 'neighbors': ['dest']},
    'dest': {'heuristic': 0, 'neighbors': []}
}

start_time = time.time()
path = greedy_best_first_search(graph, 'Src', 'dest')
end_time = time.time()

memory_info = psutil.Process().memory_info()
memory_consumed = memory_info.rss / 1024  # in KB

print("Path found:", path)
print("MAC Address:", get_mac_address())
print("Time consumed:", end_time - start_time, "seconds")
print("Memory consumed:", memory_consumed, "KB")

