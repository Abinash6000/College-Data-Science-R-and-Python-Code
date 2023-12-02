import pandas as pd
from scipy.stats import ttest_rel


def calculate_statistics(pre, post):
    # T-test
    t_statistic, p_value = ttest_rel(pre, post)

    return t_statistic, p_value

def read_excel(file_path):
    # Read excel file
    df = pd.read_excel(file_path)

    # Data is in a column named 'close'
    pre = df['Pre_Score']
    post = df['Post_Score']

    return pre, post

pre, post = read_excel('Pre_Post_Score.xlsx')
t_stat, p_value = calculate_statistics(pre, post)

print("T-Statistic: ", t_stat)
print("P-Value: ", p_value)