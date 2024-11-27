import re
import time
import uuid
import psutil

def check_sentence(sentence):
    # Rule 1: Sentence starts with capital letter
    if not sentence[0].isupper():
        return False
    
    # Rule 2: Sentence ends with proper punctuation
    if not re.match(r'.*[.?!]$', sentence):
        return False
    
    # Rule 3: No consecutive spaces
    if '  ' in sentence:
        return False
    
    # Rule 4: No digits in the sentence
    if any(char.isdigit() for char in sentence):
        return False
    
    # Rule 5: Words separated by single space only
    words = sentence.split(' ')
    if any(word == '' for word in words):
        return False
    
    return True

# Get MAC address of system
def get_mac_address():
    mac = ':'.join(re.findall('..', '%012x' % uuid.getnode()))
    return mac

# Check memory consumption
def check_memory_consumption():
    process = psutil.Process()
    memory_info = process.memory_info()
    return memory_info.rss  # Return resident set size

# Main function to execute the program logic 
def main():
    input_sentence = input("Enter a sentence to check: ")
    
    start_time = time.time() 
    
    result = check_sentence(input_sentence)
    
    end_time = time.time()
    
    print(f"Sentence is {'correct' if result else 'incorrect'}")
    
    print(f"MAC Address: {get_mac_address()}")
    
    memory_consumed = check_memory_consumption()
    print(f"Memory Consumed: {memory_consumed} bytes")
    
    time_consumed = end_time - start_time
    print(f"Time Consumed: {time_consumed} seconds")

if __name__ == "__main__":
    main()

