import pandas as pd
from sklearn.model_selection import cross_val_score
from sklearn.neighbors import KNeighborsClassifier
import time
import psutil
import uuid

# Load dataset
data = pd.read_csv('time_series_data_human_activities.csv')

# Preprocess data if necessary (e.g., normalization)
# Assuming 'x-axis', 'y-axis', and 'z-axis' are the features and 'activity' is the target
X = data[['x-axis', 'y-axis', 'z-axis']]
y = data['activity']

# Initialize KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)

# Measure memory usage before cross-validation
process = psutil.Process()
memory_before = process.memory_info().rss

# Measure time before cross-validation
start_time = time.time()

# Perform cross-validation
cv_scores = cross_val_score(knn, X, y, cv=5)

# Measure time after cross-validation
end_time = time.time()

# Measure memory usage after cross-validation
memory_after = process.memory_info().rss

# Calculate memory consumed and time taken
memory_consumed = memory_after - memory_before
time_taken = end_time - start_time

# Get MAC address
mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 8)][::-1])

print("Cross-validation scores:", cv_scores)
print("Memory consumed (bytes):", memory_consumed)
print("Time taken (seconds):", time_taken)
print("MAC address:", mac_address)

