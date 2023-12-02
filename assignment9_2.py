# nonsmok, onepack, twopack

import pandas as pd
from scipy.stats import f_oneway

data = pd.read_excel("data2.xlsx")
a = data["nonsmok"]
b = data["onepack"]
c = data["twopack"]

print(f_oneway(a, b, c))