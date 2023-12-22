import pandas as pd
file_path = "C:/Users/admin/Downloads/-ve correlation 1.xlsx"
df = pd.read_excel(file_path)
corrmat = df.corr()
corrmat
X = df["X"]
Y = df["Y"]
import matplotlib.pyplot as plt
plt.scatter(X,Y, color = 'red')
plt.title('Negative Correlation')
plt.xlabel("X values")
plt.ylabel("Y Values")
plt.show()