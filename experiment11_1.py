import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns

file_path = "C:/Users/admin/Downloads/Auto_Sales.xlsx"
df = pd.read_excel(file_path)

X = df.iloc[:,0:-1].values
Y = df.iloc[:,-1].values

print("Description")
print(df.describe())
print("\nInfo")
print(df.info())

plt.scatter(X,Y, color = "red")
plt.title("Scatter Plot")
plt.xlabel("TV_Ads")
plt.ylabel("Cars_Sold")
plt.show()

plt.boxplot(df['TV_Ads'])
plt.show()
plt.boxplot(df['Cars_Sold'])
plt.show()

X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.3, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)
print("Intercept:\n", regressor.intercept_)
print("Coefficients:\n", regressor.coef_)
