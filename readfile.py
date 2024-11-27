import pandas as pd
import matplotlib.pyplot 
import time
import os
import psutil
  

from uuid import getnode

def read_csv_and_process(file_name, attribute):
    start_time = time.time()
    
    # Read CSV file into DataFrame
    df = pd.read_csv(file_name)

    # Remove missing (NaN) values and NULL values
    df.dropna(inplace=True)
    
    # Calculate mean, mode, and median of the specified attribute
    mean_value = df[attribute].mean()
    mode_value = df[attribute].mode()[0]  # Mode could return multiple values; take the first one.
    median_value = df[attribute].median()

    # Print mean, mode, and median
    print(f"Mean of {attribute}: {mean_value}")
    print(f"Mode of {attribute}: {mode_value}")
    print(f"Median of {attribute}: {median_value}")

    # Print MAC address (physical hardware address)
    mac_address = ':'.join(['{:02x}'.format((getnode() >> elements) & 0xff) 
                            for elements in range(0, 2*6, 2)][::-1])
    print(f"MAC Address: {mac_address}")

    # Print memory consumed by this process
    process = psutil.Process(os.getpid())
    memory_consumed = process.memory_info().rss  # in bytes 
    print(f"Memory Consumed: {memory_consumed / (1024 * 1024)} MB")

    # Print time consumed by this process so far
    end_time = time.time()
    print(f"Time Consumed: {end_time - start_time} seconds")

    # Visualize the specified attribute using a histogram plot
    matplotlib.pyplot.hist(df[attribute], bins=30, edgecolor='black')
    matplotlib.pyplot.title(f'Histogram of {attribute}')
    matplotlib.pyplot.xlabel(attribute)
    matplotlib.pyplot.ylabel('Frequency')
    #plt.show()
    matplotlib.pyplot.show()
    matplotlib.use('TkAgg')

# Example usage
file_name = 'athlete_events.csv'  # Replace with your CSV file name
attribute = 'Height'  # Replace with the column name you want to analyze
read_csv_and_process(file_name, attribute)

