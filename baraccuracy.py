import pandas as pd
import numpy as np
import time
import psutil
import uuid
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Load the dataset
df = pd.read_csv('time_series_data_human_activities.csv')

# Preprocess the data
X = df[['x-axis', 'y-axis', 'z-axis']]
y = df['activity']
le = LabelEncoder()
y = le.fit_transform(y)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize classifiers
knn = KNeighborsClassifier(n_neighbors=5)
dt = DecisionTreeClassifier()

# Measure time and memory before training
start_time = time.time()
start_memory = psutil.Process().memory_info().rss

# Train and predict with kNN
knn.fit(X_train, y_train)
y_pred_knn = knn.predict(X_test)
accuracy_knn = accuracy_score(y_test, y_pred_knn)

# Train and predict with Decision Tree
dt.fit(X_train, y_train)
y_pred_dt = dt.predict(X_test)
accuracy_dt = accuracy_score(y_test, y_pred_dt)

# Measure time and memory after training
end_time = time.time()
end_memory = psutil.Process().memory_info().rss

# Calculate time and memory consumed
time_consumed = end_time - start_time
memory_consumed = end_memory - start_memory

# Get MAC address
mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1])

# Print results
print(f"MAC Address: {mac_address}")
print(f"Memory Consumed: {memory_consumed / (1024 ** 2):.2f} MB")
print(f"Time Consumed: {time_consumed:.2f} seconds")
print(f"Accuracy of kNN: {accuracy_knn:.2f}")
print(f"Accuracy of Decision Tree: {accuracy_dt:.2f}")

# Plot the accuracies
labels = ['kNN', 'Decision Tree']
accuracies = [accuracy_knn, accuracy_dt]

plt.bar(labels, accuracies, color=['blue', 'green'])
plt.xlabel('Classifier')
plt.ylabel('Accuracy')
plt.title('Accuracy Comparison')
plt.ylim(0, 1)
plt.show()

