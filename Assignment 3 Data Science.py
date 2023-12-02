import pandas as pd

# Function to calculate mean, median, mode, standard deviation, variance, and coefficient of variation
def calculate_statistics(data):
    # Mean
    mean_value = data.mean()

    # Median
    median_value = data.median()

    # Mode
    mode_value = data.mode().iloc[0]  # Use iloc[0] to get the first mode if there are multiple modes

    # Standard Deviation
    std_deviation = data.std()

    # Variance
    variance_value = data.var()

    # Coefficient of Variation (CV)
    coefficient_of_variation = (std_deviation / mean_value) * 100

    return mean_value, median_value, mode_value, std_deviation, variance_value, coefficient_of_variation

# Read excel
def read_csv(file_path):
    # Read excel file
    df = pd.read_excel(file_path)

    # Data is in a column named 'Data'
    data = df['Data']

    # Call function to calculate
    mean, median, mode, std_dev, variance, cv = calculate_statistics(data)

    # Print
    print(f"Mean: {mean}")
    print(f"Median: {median}")
    print(f"Mode: {mode}")
    print(f"Standard Deviation: {std_dev}")
    print(f"Variance: {variance}")
    print(f"Coefficient of Variation: {cv}%")

def calculate_covariance(file1_path, file2_path):
    # Read the Excel files into pandas DataFrames
    df1 = pd.read_excel(file1_path)
    df2 = pd.read_excel(file2_path)

    data1 = df1['Data']
    data2 = df2['Data']
    
    # Calculate the covariance between the two DataFrames
    covariance = data1.cov(data2)
    
    return covariance

def main():
    # Read 1st excel file
    read_csv('RandomData1.xlsx')

    print('\n\n')

    # Read 2nd excel file
    read_csv('RandomData2.xlsx')

    print('\n\n')

    # Find covariance between two excel files
    cov = calculate_covariance('RandomData1.xlsx', 'RandomData2.xlsx')
    print(f"Covariance: {cov}\n\n")


main()