import numpy as np
from sklearn.preprocessing import MinMaxScaler

data = np.array([8, 10, 15, 20]).reshape(-1, 1)

scaler = MinMaxScaler()
min_max = scaler.fit_transform(data)
print(min_max)

scaled_data = scaler.transform(data)
print(scaled_data)
