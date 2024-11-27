import time
import psutil
import uuid

# Define the map of Australia with its territories and their neighbors
australia_map = {
    'Western Australia':('Northern Territory','South Australia'),
    'Northern Territory':('Western Australia','South Australia','Queensland'),
    'South Australia':('Western Australia','Northern Territory','Queensland','New South Wales','Victoria'),
    'Queensland':('Northern Territory','South Australia','New South Wales'),
    'Victoria':('South Australia','New South Wales'),
    'New South Wales':('Queensland','South Australia','Victoria'),
    'Tasmania':() # Tasmania has no adjacent territories
}
# Define the colors
colors = ['Red', 'Green', 'Blue']

# Function to check if the current color assignment is safe
def is_safe(territory, color, color_assignment):
    for neighbor in australia_map[territory]:
        if color_assignment.get(neighbor) == color:
            return False
    return True

# Function to solve the map coloring problem using backtracking
def color_map(territory_index, color_assignment):
    if territory_index == len(australia_map):
        return True

    territory = list(australia_map.keys())[territory_index]
    for color in colors:
        if is_safe(territory, color, color_assignment):
            color_assignment[territory] = color
            if color_map(territory_index + 1, color_assignment):
                return True
            color_assignment[territory] = None

    return False

# Main function
def main():
    start_time = time.time()
    color_assignment = {territory: None for territory in australia_map}
    if color_map(0, color_assignment):
        print("Coloring of the map is possible:")
        for territory, color in color_assignment.items():
            print(f"{territory}: {color}")
    else:
        print("Coloring of the map is not possible.")

    end_time = time.time()
    time_consumed = end_time - start_time
    memory_consumed = psutil.Process().memory_info().rss / 1024 ** 2  # Memory in MB
    mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1])

    print(f"\nTime consumed: {time_consumed:.4f} seconds")
    print(f"Memory consumed: {memory_consumed:.4f} MB")
    print(f"MAC Address: {mac_address}")

if __name__ == "__main__":
    main()

