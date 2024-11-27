import itertools
import time
import sys
import uuid

def generate_passwords(length, chars):
    return [''.join(p) for p in itertools.product(chars, repeat=length)]

def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0, 11, 2)])

def main():
    length = int(input("Enter the desired length for passwords: "))
    chars = input("Enter the desired character set for passwords: ")
    
    start_time = time.time()
    passwords = generate_passwords(length, chars)
    end_time = time.time()
    
    memory_used = sys.getsizeof(passwords)
    
    mac_address = get_mac_address()
    
    print(f"Generated {len(passwords)} unique passwords.")
    print(f"Memory consumed: {memory_used} bytes")
    print(f"Time consumed: {end_time - start_time} seconds")
    print(f"MAC Address: {mac_address}")
    print(passwords)
    
    return passwords

# Example usage:
if __name__ == "__main__":
    generated_passwords_list = main()

