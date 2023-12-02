import pandas as pd
from scipy.stats import ttest_ind


def calculate_statistics(female, male):
    # T-test
    t_statistic, p_value = ttest_ind(female, male)

    return t_statistic, p_value

def read_excel(file_path):
    # Read excel file
    df = pd.read_excel(file_path, sheet_name='Sheet1')

    # Data is in a column named 'close'
    female = df['Apple']
    male = df['Samsung']

    return female, male

female, male = read_excel('Iphone_Response_Data.xlsx')
t_stat, p_value = calculate_statistics(female, male)

print("T-Statistic: ", t_stat)
print("P-Value: ", p_value)