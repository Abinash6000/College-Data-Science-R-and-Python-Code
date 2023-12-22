import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
data = np.array([[2.5,2.4], [0.5,0.7], [2.2,2.9], [1.9,2.2],[3.13,0], [2.3,2.7],[2.0,1.6],[1.0,1.1],[1.5,1.6], [1.1,0.9], [2.0,1.6]])
print(data)
df = pd.DataFrame(data, columns = ['X1', 'X2'])
print(df)
df.mean()
cov_matrix = np.cov(df.values.T)
print(cov_matrix)
eigen_values, eigen_vectors = np.linalg.eig(cov_matrix)
print(eigen_values)
print(eigen_vectors)
from sklearn.decomposition import PCA
pca = PCA(n_components=1)
pca.fit(df)
transformed_data = pca.transform(df)
print(transformed_data)
pca = PCA(n_components=2)
pca.fit(df)
transformed_data = pca.transform(df)
print(transformed_data)
X_reconstructed = pca.inverse_transform(transformed_data)
print(X_reconstructed)