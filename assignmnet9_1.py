# lecture, qa, library

import pandas as pd
from scipy.stats import f_oneway

data = pd.read_excel(r"C:\Users\admin\OneDrive\Desktop\VIT\Sem 4\Foundataion of Data Science\R and Python Codes\data1.xlsx")
a = data["lecture"]
b = data["qa"]
c = data["library"]

print(f_oneway(a, b, c))