import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = "C:/Users/admin/Downloads/+ve correlation 1.xlsx"
df = pd.read_excel(file_path)

X = df["X"]
Y = df["Y"]

correlation_coefficient = np.corrcoef(X, Y)[0, 1]
print("Correlation Coefficient:", correlation_coefficient)

plt.scatter(X, Y, color='red')
plt.title('Positive Correlation')
plt.xlabel("X values")
plt.ylabel("Y Values")
plt.show()

