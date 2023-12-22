# OLS (Ordinary Least Square Method) for model 1
# Ordinary Least Squares (OLS) is a method used in linear regression
# to estimate the parameters of a linear regression model. 
# The goal of OLS is to find the line (or hyperplane in the case of multiple variables) 
# that minimizes the sum of the squared differences between the observed and predicted values.
# In other words, it finds the coefficients for the linear equation that best fits the given data.

from sklearn.model_selection import train_test_split
import pandas as pd
import pandas as pd
import statsmodels.api as sm

mark_data = pd.read_excel(r"C:\Users\admin\Downloads\Marketing_Data.xlsx")

# Model 1
X1 = mark_data[['youtube','facebook']]
Y1 = mark_data['sales']
X_train1, X_test1, Y_train1, Y_test1 = train_test_split(X1, Y1, test_size=0.3, random_state=0)

# OLS (Ordinary Least Square Method) for model 1
X_train1 = sm.add_constant(X_train1)
X_test1 = sm.add_constant(X_test1)
print("\n\n")
model = sm.OLS(Y_train1, X_train1).fit()

# Make predictions on the testing set
Y_Pred1 = model.predict(X_test1)

# Print the regression coefficients/parameters
print(model.params,"\n")
print("Regression Line y1 = ",round(model.params[1], 3),"* youtube + ",round(model.params[2], 3),"* facebook + ",round(model.params[0], 3))
print("\n\n")

# Create a DataFrame to display the data in a table-like format
results = pd.DataFrame({'Y_test1': Y_test1[:5], 'Y_Pred1': Y_Pred1[:5], 'Y_test1 - Y_Pred1': Y_test1[:5] - Y_Pred1[:5]})

# Display the DataFrame
print(results)