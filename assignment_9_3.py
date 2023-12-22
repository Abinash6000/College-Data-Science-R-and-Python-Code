# buff, pitt, detr

import pandas as pd
from scipy.stats import f_oneway

data = pd.read_excel(r"C:\Users\admin\OneDrive\Desktop\VIT\Sem 4\Foundataion of Data Science\R and Python Codes\data3.xlsx")
a = data["buff"]
b = data["pitt"]
c = data["detr"]

print(f_oneway(a, b, c))