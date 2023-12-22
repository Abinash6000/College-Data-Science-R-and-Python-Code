import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

Depression_Data = pd.read_excel(r"C:\Users\admin\OneDrive\Desktop\VIT\Sem 4\Foundataion of Data Science\R and Python Codes\Depression_Data.xlsx")
# sns.boxplot(x='Mothers_Education', y='PD', data=Depression_Data, width=0.5)
# sns.boxplot(x='Mothers_Education', y='GD', data=Depression_Data, width=0.5)
sns.boxplot(x='Mothers_Education', y='SC', data=Depression_Data, width=0.5)
plt.show()