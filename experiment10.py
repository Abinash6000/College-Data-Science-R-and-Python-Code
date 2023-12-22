import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
file_path = "C:/Users/admin/Downloads/data2_PCA.xlsx"
df = pd.read_excel(file_path)
print(df)
df.mean()
cov_matrix = np.cov(df.values.T)
print("covariance matrix:", cov_matrix)
eigen_values, eigen_vectors = np.linalg.eig(cov_matrix)
print("eigen values:", eigen_values)
print("eigen vectors:", eigen_vectors)
from sklearn.decomposition import PCA
pca = PCA(n_components=1)
pca.fit(df)
transformed_data = pca.transform(df)
print("transformed data:", transformed_data)
pca = PCA(n_components=2)
pca.fit(df)
transformed_data = pca.transform(df)
print("transformed data:", transformed_data)
X_reconstructed = pca.inverse_transform(transformed_data)
print("reconstructed data:", X_reconstructed)