import time
import psutil
import uuid
import os

def get_mac_address():
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 8*6, 8)][::-1])
    return mac

def water_jug_problem():
    # Initial state (0, 0)
    jug1, jug2 = 0, 0
    steps = []

    # Fill the 3-gallon jug
    jug2 = 3
    steps.append((jug1, jug2))

    # Pour water from the 3-gallon jug into the 4-gallon jug
    jug1, jug2 = jug2, 0
    steps.append((jug1, jug2))

    # Fill the 3-gallon jug again
    jug2 = 3
    steps.append((jug1, jug2))

    # Pour water from the 3-gallon jug into the 4-gallon jug until the 4-gallon jug is full
    jug1, jug2 = 4, jug2 - (4 - jug1)
    steps.append((jug1, jug2))

    # Empty the 4-gallon jug
    jug1 = 0
    steps.append((jug1, jug2))

    # Pour the remaining water from the 3-gallon jug into the 4-gallon jug
    jug1, jug2 = jug2, 0
    steps.append((jug1, jug2))

    # Fill the 3-gallon jug again
    jug2 = 3
    steps.append((jug1, jug2))

    # Pour water from the 3-gallon jug into the 4-gallon jug until there are exactly 2 gallons in the 4-gallon jug
    jug1, jug2 = jug1 + jug2, 0
    steps.append((jug1, jug2))

    return steps

def main():
    start_time = time.time()
    steps = water_jug_problem()
    end_time = time.time()

    memory_info = psutil.Process(os.getpid()).memory_info()
    memory_used = memory_info.rss / (1024 ** 2)  # Convert bytes to MB

    mac_address = get_mac_address()

    print("Steps to solve the Water Jug Problem:")
    for step in steps:
        print(step)

    print(f"\nMAC Address: {mac_address}")
    print(f"Memory Used: {memory_used:.2f} MB")
    print(f"Time Taken: {end_time - start_time:.4f} seconds")

if __name__ == "__main__":
    main()

