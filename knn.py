import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, roc_curve, roc_auc_score
import time
import psutil
import uuid
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv('time_series_data_human_activities.csv')

# Preprocess dataset (assuming 'activity' is the target variable)
X = data.drop(['activity', 'user', 'timestamp'], axis=1)
y = data['activity']

# Split dataset into training set and test set
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create KNN classifier
knn = KNeighborsClassifier(n_neighbors=3)

# Record start time and memory usage before training model
start_time = time.time()
memory_before = psutil.Process().memory_info().rss / (1024 * 1024)

# Train the classifier using the training set
knn.fit(X_train, y_train)

# Predict on test set 
y_pred = knn.predict(X_test)

# Record end time and memory usage after prediction 
end_time = time.time()
memory_after = psutil.Process().memory_info().rss / (1024 * 1024)

# Calculate accuracy 
accuracy = accuracy_score(y_test, y_pred)

# Compute confusion matrix 
conf_matrix = confusion_matrix(y_test, y_pred)

# Compute ROC curve and ROC area for each class
y_prob = knn.predict_proba(X_test)
roc_auc = roc_auc_score(y_test, y_prob, multi_class='ovr')

# Plot ROC curve
fpr = {}
tpr = {}
thresh = {}
for i in range(len(knn.classes_)):
    fpr[i], tpr[i], thresh[i] = roc_curve(y_test, y_prob[:, i], pos_label=knn.classes_[i])

plt.figure(figsize=(10, 8))
for i in range(len(knn.classes_)):
    plt.plot(fpr[i], tpr[i], linestyle='--', label=f'{knn.classes_[i]} vs Rest')
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Multiclass ROC curve')
plt.legend(loc='best')
plt.show()

# Get MAC address
mac_address = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2*6, 2)][::-1])

# Print results
print(f"Accuracy: {accuracy}")
print(f"Confusion Matrix:\n{conf_matrix}")
print(f"ROC AUC Score: {roc_auc}")
print(f"MAC Address: {mac_address}")
print(f"Memory Consumed: {memory_after - memory_before} MB")
print(f"Time Consumed: {end_time - start_time} seconds")

