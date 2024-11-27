import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score
import psutil
import time
import uuid

# Function to get MAC address
def get_mac_address():
    mac = uuid.UUID(int=uuid.getnode()).hex[-12:]
    return ":".join([mac[e:e+2] for e in range(0, 11, 2)])

# Load dataset
data = pd.read_csv('time_series_data_human_activities.csv')

# Assuming that the target variable is 'activity' and rest are features
X = data.drop('activity', axis=1)
y = data['activity']

# Initialize Decision Tree Classifier
decision_tree = DecisionTreeClassifier()

# Measure memory before
process = psutil.Process()
mem_before = process.memory_info().rss / 1024 ** 2  # in MB

# Measure time before
start_time = time.time()

# Perform 10-fold cross-validation
scores = cross_val_score(decision_tree, X, y, cv=10)

# Measure time after
end_time = time.time()

# Measure memory after
mem_after = process.memory_info().rss / 1024 ** 2  # in MB

# Calculate time and memory consumed
time_consumed = end_time - start_time
memory_consumed = mem_after - mem_before

print(f'Cross-validation scores: {scores}')
print(f'Mean score: {scores.mean()}')
print(f'Time consumed: {time_consumed} seconds')
print(f'Memory consumed: {memory_consumed} MB')
print(f'MAC address: {get_mac_address()}')

