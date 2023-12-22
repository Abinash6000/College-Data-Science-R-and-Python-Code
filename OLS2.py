from sklearn.model_selection import train_test_split
import pandas as pd
import pandas as pd
import statsmodels.api as sm

mark_data = pd.read_excel(r"C:\Users\admin\Downloads\Marketing_Data.xlsx")

X = mark_data[['youtube','facebook']]
Y = mark_data['sales']
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=0)

X_train = sm.add_constant(X_train)
X_test = sm.add_constant(X_test)
print("\n\n")
model = sm.OLS(Y_train, X_train).fit()

Y_Pred = model.predict(X_test)

print(model.params,"\n")