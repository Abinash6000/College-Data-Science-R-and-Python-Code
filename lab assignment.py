from sklearn import metrics
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd

mark_data = pd.read_excel(r"C:\Users\admin\Downloads\Marketing_Data.xlsx")

# Model 1
X1 = mark_data[['youtube','facebook']]
Y1 = mark_data['sales']
X_train1, X_test1, Y_train1, Y_test1 = train_test_split(X1, Y1, test_size=0.3, random_state=0)
regressor1 = LinearRegression()
regressor1.fit(X_train1, Y_train1)
Y_Pred1 = regressor1.predict(X_test1)
print("Regression Line y1 = ",round(regressor1.coef_[0], 3),"* youtube + ",round(regressor1.coef_[1], 3),"* facebook + ",round(regressor1.intercept_, 3))

# Model 2
X2 = mark_data[['youtube','newspaper','facebook']]
Y2 = mark_data['sales']
X_train2, X_test2, Y_train2, Y_test2 = train_test_split(X2, Y2, test_size=0.3, random_state=0)
regressor2 = LinearRegression()
regressor2.fit(X_train2, Y_train2)
Y_Pred2 = regressor2.predict(X_test2)
print("Regression Line y2 = ",round(regressor2.coef_[0], 3),"* youtube + ",round(regressor2.coef_[1], 3),"* newspaper + ",round(regressor2.coef_[2], 3),"* facebook + ",round(regressor2.intercept_, 3))

# Model 3
X3 = mark_data[['youtube','newspaper']]
Y3 = mark_data['sales']
X_train3, X_test3, Y_train3, Y_test3 = train_test_split(X3, Y3, test_size=0.3, random_state=0)
regressor3 = LinearRegression()
regressor3.fit(X_train3, Y_train3)
Y_Pred3 = regressor3.predict(X_test3)
print("Regression Line y3 = ",round(regressor3.coef_[0], 3),"* youtube + ",round(regressor3.coef_[1], 3),"* newspaper + ",round(regressor3.intercept_, 3))

# Model 4
X4 = mark_data[['newspaper','facebook']]
Y4 = mark_data['sales']
X_train4, X_test4, Y_train4, Y_test4 = train_test_split(X4, Y4, test_size=0.3, random_state=0)
regressor4 = LinearRegression()
regressor4.fit(X_train4, Y_train4)
Y_Pred4 = regressor4.predict(X_test4)
print("Regression Line y4 = ",round(regressor4.coef_[0], 3),"* newspaper + ",round(regressor4.coef_[1], 3),"* facebook + ",round(regressor4.intercept_, 3))

# Model 5
X5 = mark_data[['youtube']]
Y5 = mark_data['sales']
X_train5, X_test5, Y_train5, Y_test5 = train_test_split(X5, Y5, test_size=0.3, random_state=0)
regressor5 = LinearRegression()
regressor5.fit(X_train5, Y_train5)
Y_Pred5 = regressor5.predict(X_test5)
print("Regression Line y5 = ",round(regressor5.coef_[0], 3),"* youtube + ",round(regressor5.intercept_, 3))

# Model 6
X6 = mark_data[['newspaper']]
Y6 = mark_data['sales']
X_train6, X_test6, Y_train6, Y_test6 = train_test_split(X6, Y6, test_size=0.3, random_state=0)
regressor6 = LinearRegression()
regressor6.fit(X_train6, Y_train6)
Y_Pred6 = regressor6.predict(X_test6)
print("Regression Line y6 = ",round(regressor6.coef_[0], 3),"* newspaper + ",round(regressor6.intercept_, 3))

# Model 7
X7 = mark_data[['facebook']]
Y7 = mark_data['sales']
X_train7, X_test7, Y_train7, Y_test7 = train_test_split(X7, Y7, test_size=0.3, random_state=0)
regressor7 = LinearRegression()
regressor7.fit(X_train7, Y_train7)
Y_Pred7 = regressor7.predict(X_test7)
print("Regression Line y7 = ",round(regressor7.coef_[0], 3),"* facebook + ",round(regressor7.intercept_, 3))

# Finding Multiple R
Multiple_R1 = metrics.r2_score(Y_test1, Y_Pred1)
Multiple_R2 = metrics.r2_score(Y_test2, Y_Pred2)
Multiple_R3 = metrics.r2_score(Y_test3, Y_Pred3)
Multiple_R4 = metrics.r2_score(Y_test4, Y_Pred4)
Multiple_R5 = metrics.r2_score(Y_test5, Y_Pred5)
Multiple_R6 = metrics.r2_score(Y_test6, Y_Pred6)
Multiple_R7 = metrics.r2_score(Y_test7, Y_Pred7)

# Finding R Square
R_Square1 = Multiple_R1**2
R_Square2 = Multiple_R2**2
R_Square3 = Multiple_R3**2
R_Square4 = Multiple_R4**2
R_Square5 = Multiple_R5**2
R_Square6 = Multiple_R6**2
R_Square7 = Multiple_R7**2

# Finding Adjusted R Square
n1 = len(Y_test1) # no. of observations
p1 = X_test1.shape[1] # no. of predictors
Adjusted_R_Square1 = 1-(1-Multiple_R1)*(n1-1)/(n1-p1-1)

n2 = len(Y_test2)
p2 = X_test2.shape[1]
Adjusted_R_Square2 = 1-(1-Multiple_R2)*(n2-1)/(n2-p2-1)

n3 = len(Y_test3)
p3 = X_test3.shape[1]
Adjusted_R_Square3 = 1-(1-Multiple_R3)*(n3-1)/(n3-p3-1)

n4 = len(Y_test4)
p4 = X_test4.shape[1]
Adjusted_R_Square4 = 1-(1-Multiple_R4)*(n4-1)/(n4-p4-1)

n5 = len(Y_test5)
p5 = X_test5.shape[1]
Adjusted_R_Square5 = 1-(1-Multiple_R5)*(n5-1)/(n5-p5-1)

n6 = len(Y_test6)
p6 = X_test6.shape[1]
Adjusted_R_Square6 = 1-(1-Multiple_R6)*(n6-1)/(n6-p6-1)

n7 = len(Y_test7)
p7 = X_test7.shape[1]
Adjusted_R_Square7 = 1-(1-Multiple_R7)*(n7-1)/(n7-p7-1)

# Fniding Standard Error of Estimate

SEE1 = np.sqrt(metrics.mean_squared_error(Y_test1, Y_Pred1))
SEE2 = np.sqrt(metrics.mean_squared_error(Y_test2, Y_Pred2))
SEE3 = np.sqrt(metrics.mean_squared_error(Y_test3, Y_Pred3))
SEE4 = np.sqrt(metrics.mean_squared_error(Y_test4, Y_Pred4))
SEE5 = np.sqrt(metrics.mean_squared_error(Y_test5, Y_Pred5))
SEE6 = np.sqrt(metrics.mean_squared_error(Y_test6, Y_Pred6))
SEE7 = np.sqrt(metrics.mean_squared_error(Y_test7, Y_Pred7))

# Finding ANNOVA: F-Statistic

n = len(Y_test1)
p = X_test1.shape[1]
F_Statistic1 = (Multiple_R1/(1-Multiple_R1))*((n-p-1)/p)

n = len(Y_test2)
p = X_test2.shape[1]
F_Statistic2 = (Multiple_R2/(1-Multiple_R2))*((n-p-1)/p)

n = len(Y_test3)
p = X_test3.shape[1]
F_Statistic3 = (Multiple_R3/(1-Multiple_R3))*((n-p-1)/p)

n = len(Y_test4)
p = X_test4.shape[1]
F_Statistic4 = (Multiple_R4/(1-Multiple_R4))*((n-p-1)/p)

n = len(Y_test5)
p = X_test5.shape[1]
F_Statistic5 = (Multiple_R5/(1-Multiple_R5))*((n-p-1)/p)

n = len(Y_test6)
p = X_test6.shape[1]
F_Statistic6 = (Multiple_R6/(1-Multiple_R6))*((n-p-1)/p)

n = len(Y_test7)
p = X_test7.shape[1]
F_Statistic7 = (Multiple_R7/(1-Multiple_R7))*((n-p-1)/p)

# Create a dictionary with the model names as keys and the corresponding metrics as values
metrics_dict = {
    'Model 1': [Multiple_R1, R_Square1, Adjusted_R_Square1, SEE1, F_Statistic1],
    'Model 2': [Multiple_R2, R_Square2, Adjusted_R_Square2, SEE2, F_Statistic2],
    'Model 3': [Multiple_R3, R_Square3, Adjusted_R_Square3, SEE3, F_Statistic3],
    'Model 4': [Multiple_R4, R_Square4, Adjusted_R_Square4, SEE4, F_Statistic4],
    'Model 5': [Multiple_R5, R_Square5, Adjusted_R_Square5, SEE5, F_Statistic5],
    'Model 6': [Multiple_R6, R_Square6, Adjusted_R_Square6, SEE6, F_Statistic6],
    'Model 7': [Multiple_R7, R_Square7, Adjusted_R_Square7, SEE7, F_Statistic7]
}

# Create a DataFrame from the dictionary
print("\n\n")
df = pd.DataFrame.from_dict(metrics_dict, orient='index', columns=['Multiple R', 'R Square', 'Adjusted R Square', 'Standard Error', 'ANNOVA: F'])

# Display the DataFrame
print(df)
print("\n\n")

# Finding MSE (Mean Squared Error)
MSE1 = metrics.mean_squared_error(Y_test1, Y_Pred1)
MSE2 = metrics.mean_squared_error(Y_test2, Y_Pred2)
MSE3 = metrics.mean_squared_error(Y_test3, Y_Pred3)
MSE4 = metrics.mean_squared_error(Y_test4, Y_Pred4)
MSE5 = metrics.mean_squared_error(Y_test5, Y_Pred5)
MSE6 = metrics.mean_squared_error(Y_test6, Y_Pred6)
MSE7 = metrics.mean_squared_error(Y_test7, Y_Pred7)

# Finding RMSE (Root Mean Squared Error)
RMSE1 = np.sqrt(metrics.mean_squared_error(Y_test1, Y_Pred1))
RMSE2 = np.sqrt(metrics.mean_squared_error(Y_test2, Y_Pred2))
RMSE3 = np.sqrt(metrics.mean_squared_error(Y_test3, Y_Pred3))
RMSE4 = np.sqrt(metrics.mean_squared_error(Y_test4, Y_Pred4))
RMSE5 = np.sqrt(metrics.mean_squared_error(Y_test5, Y_Pred5))
RMSE6 = np.sqrt(metrics.mean_squared_error(Y_test6, Y_Pred6))
RMSE7 = np.sqrt(metrics.mean_squared_error(Y_test7, Y_Pred7))

# Finding MAE (Mean Absolute Error)
MAE1 = metrics.mean_absolute_error(Y_test1, Y_Pred1)
MAE2 = metrics.mean_absolute_error(Y_test2, Y_Pred2)
MAE3 = metrics.mean_absolute_error(Y_test3, Y_Pred3)
MAE4 = metrics.mean_absolute_error(Y_test4, Y_Pred4)
MAE5 = metrics.mean_absolute_error(Y_test5, Y_Pred5)
MAE6 = metrics.mean_absolute_error(Y_test6, Y_Pred6)
MAE7 = metrics.mean_absolute_error(Y_test7, Y_Pred7)

# Finding MAPE (Mean Absolute Percentage Error)
MAPE1 = np.mean(np.abs((Y_test1 - Y_Pred1) / Y_test1)) * 100
MAPE2 = np.mean(np.abs((Y_test2 - Y_Pred2) / Y_test2)) * 100
MAPE3 = np.mean(np.abs((Y_test3 - Y_Pred3) / Y_test3)) * 100
MAPE4 = np.mean(np.abs((Y_test4 - Y_Pred4) / Y_test4)) * 100
MAPE5 = np.mean(np.abs((Y_test5 - Y_Pred5) / Y_test5)) * 100
MAPE6 = np.mean(np.abs((Y_test6 - Y_Pred6) / Y_test6)) * 100
MAPE7 = np.mean(np.abs((Y_test7 - Y_Pred7) / Y_test7)) * 100

# Finding MPE (Mean Percentage Error)
MPE1 = np.mean((Y_test1 - Y_Pred1) / Y_test1) * 100
MPE2 = np.mean((Y_test2 - Y_Pred2) / Y_test2) * 100
MPE3 = np.mean((Y_test3 - Y_Pred3) / Y_test3) * 100
MPE4 = np.mean((Y_test4 - Y_Pred4) / Y_test4) * 100
MPE5 = np.mean((Y_test5 - Y_Pred5) / Y_test5) * 100
MPE6 = np.mean((Y_test6 - Y_Pred6) / Y_test6) * 100
MPE7 = np.mean((Y_test7 - Y_Pred7) / Y_test7) * 100

# Create a dictionary with the model names as keys and the corresponding metrics as values
metrics_dict = {
    'Model 1': [MSE1, RMSE1, MAE1, MAPE1, MPE1],
    'Model 2': [MSE2, RMSE2, MAE2, MAPE2, MPE2],
    'Model 3': [MSE3, RMSE3, MAE3, MAPE3, MPE3],
    'Model 4': [MSE4, RMSE4, MAE4, MAPE4, MPE4],
    'Model 5': [MSE5, RMSE5, MAE5, MAPE5, MPE5],
    'Model 6': [MSE6, RMSE6, MAE6, MAPE6, MPE6],
    'Model 7': [MSE7, RMSE7, MAE7, MAPE7, MPE7]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame.from_dict(metrics_dict, orient='index', columns=['MSE', 'RMSE', 'MAE', 'MAPE', 'MPE'])

# Display the DataFrame
print(df)


# Finding AIC (Akaike Information Criterion)
AIC1 = 2*(3+1)-2*np.log(MSE1)
AIC2 = 2*(4+1)-2*np.log(MSE2)
AIC3 = 2*(3+1)-2*np.log(MSE3)
AIC4 = 2*(3+1)-2*np.log(MSE4)
AIC5 = 2*(2+1)-2*np.log(MSE5)
AIC6 = 2*(2+1)-2*np.log(MSE6)
AIC7 = 2*(2+1)-2*np.log(MSE7)

# Finding BIC (Bayesian Information Criterion)
BIC1 = np.log(n1)*(3+1)-2*np.log(MSE1)
BIC2 = np.log(n2)*(4+1)-2*np.log(MSE2)
BIC3 = np.log(n3)*(3+1)-2*np.log(MSE3)
BIC4 = np.log(n4)*(3+1)-2*np.log(MSE4)
BIC5 = np.log(n5)*(2+1)-2*np.log(MSE5)
BIC6 = np.log(n6)*(2+1)-2*np.log(MSE6)
BIC7 = np.log(n7)*(2+1)-2*np.log(MSE7)

# Create a dictionary with the model names as keys and the corresponding metrics as values
metrics_dict = {
    'Model 1': [AIC1, BIC1],
    'Model 2': [AIC2, BIC2],
    'Model 3': [AIC3, BIC3],
    'Model 4': [AIC4, BIC4],
    'Model 5': [AIC5, BIC5],
    'Model 6': [AIC6, BIC6],
    'Model 7': [AIC7, BIC7]
}

# Create a DataFrame from the dictionary
df = pd.DataFrame.from_dict(metrics_dict, orient='index', columns=['AIC', 'BIC'])

# Display the DataFrame
print("\n\n")
print(df)

# Residual Vs Predicted Scatter Plot
import matplotlib.pyplot as plt
# plt.scatter(Y_Pred1, Y_test1-Y_Pred1, color='red')
# plt.title('Residual Vs Predicted (Model 1)')
# plt.xlabel('Predicted')
# plt.ylabel('Residual')
# plt.show()

# plt.scatter(Y_Pred2, Y_test2-Y_Pred2, color='red')
# plt.title('Residual Vs Predicted (Model 2)')
# plt.xlabel('Predicted')
# plt.ylabel('Residual')
# plt.show()

# plt.scatter(Y_Pred3, Y_test3-Y_Pred3, color='red')
# plt.title('Residual Vs Predicted (Model 3)')
# plt.xlabel('Predicted')
# plt.ylabel('Residual')
# plt.show()

# plt.scatter(Y_Pred4, Y_test4-Y_Pred4, color='red')
# plt.title('Residual Vs Predicted (Model 4)')
# plt.xlabel('Predicted')
# plt.ylabel('Residual')
# plt.show()

# plt.scatter(Y_Pred5, Y_test5-Y_Pred5, color='red')
# plt.title('Residual Vs Predicted (Model 5)')
# plt.xlabel('Predicted')
# plt.ylabel('Residual')
# plt.show()

# plt.scatter(Y_Pred6, Y_test6-Y_Pred6, color='red')
# plt.title('Residual Vs Predicted (Model 6)')
# plt.xlabel('Predicted')
# plt.ylabel('Residual')
# plt.show()

# plt.scatter(Y_Pred7, Y_test7-Y_Pred7, color='red')
# plt.title('Residual Vs Predicted (Model 7)')
# plt.xlabel('Predicted')
# plt.ylabel('Residual')
# plt.show()
