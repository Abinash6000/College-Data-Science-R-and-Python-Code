# buff, pitt, detr

import pandas as pd
from scipy.stats import f_oneway

data = pd.read_excel("data3.xlsx")
a = data["buff"]
b = data["pitt"]
c = data["detr"]

print(f_oneway(a, b, c))