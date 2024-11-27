import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
from keras.models import Sequential
from keras.layers import Dense
import time
import psutil
import uuid
import re

# Load the dataset from a CSV file
df = pd.read_csv('house_prices.csv')

# Preprocessing data: One-hot encoding for categorical data ('Location')
encoder = OneHotEncoder()
location_encoded = encoder.fit_transform(df[['Location']]).toarray()

# Combining numerical features with encoded categorical feature.
numerical_features = df[['Number of bedrooms', 'Carpet Area (sq. ft.)', 'Years Old']].values.astype(float)
features = np.concatenate([numerical_features, location_encoded], axis=1)
prices = df['Rent (per month Rs.)'].values.astype(float)

# Splitting dataset into training and testing sets.
X_train, X_test, y_train, y_test = train_test_split(features, prices, test_size=0.2)

# Building the deep learning model.
model = Sequential()
model.add(Dense(10, input_dim=X_train.shape[1], activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1))

model.compile(optimizer='adam', loss='mean_squared_error')

start_time = time.time()

# Training the model on our dataset.
model.fit(X_train, y_train, batch_size=10, epochs=100)

end_time = time.time()

time_consumed = end_time - start_time

memory_consumed = psutil.Process().memory_info().rss / (1024 ** 2)  # Memory in MB

mac_address = ':'.join(re.findall('..', '%012x' % uuid.getnode()))

print(f"MAC Address: {mac_address}")
print(f"Memory Consumed: {memory_consumed} MB")
print(f"Time Consumed: {time_consumed} seconds")

