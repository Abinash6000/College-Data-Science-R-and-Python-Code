import pandas as pd
from scipy.stats import ttest_ind


def calculate_statistics(data):
    # T-test
    t_statistic, p_value = ttest_ind(data, [0], alternative='two-sided')

    return t_statistic, p_value

def read_excel(file_path):
    # Read excel file
    df = pd.read_excel(file_path)

    # Data is in a column named 'close'
    data = df['Rice_Bag_Weight']

    return data

hclData = read_excel('RelianceMart.xlsx')
t_stat, p_value = calculate_statistics(hclData)

print("T-Statistic: ", t_stat)
print("P-Value: ", p_value)