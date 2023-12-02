import scipy.stats as stats
import pandas as pd

def calculate_statistics(data):
    # Mean
    mean_value = data.mean()

    # Median
    median_value = data.median()

    # Mode
    mode_value = data.mode().iloc[0]  # Use iloc[0] to get the first mode if there are multiple modes

    # Hmean
    harmonic_mean = stats.hmean(data)

    # Geometric Mean
    geometric_mean = stats.gmean(data)

    # Standard Deviation
    standard_deviation = data.std()

    # Coefficient of Variation
    coefficient_of_variation = standard_deviation / mean_value

    # Skewness
    skewness = data.skew()

    # Kurtosis
    kurtosis = data.kurtosis()

    # Data Quality
    dq = harmonic_mean / mean_value


    return mean_value, median_value, mode_value, harmonic_mean, geometric_mean, standard_deviation, coefficient_of_variation, skewness, kurtosis, dq

def read_excel(file_path):
    # Read excel file
    df = pd.read_excel(file_path)

    # Data is in a column named 'close'
    data = df['close']

    return data


sbiData = read_excel('SBI.xlsx')
sbiMean, sbiMode, sbiMedian, sbiHmean, sbiGmean, sbiStd, sbiCv, sbiSkew, sbiKurt, sbidq = calculate_statistics(sbiData)
axisbankData = read_excel('AXISBANK.xlsx')
axisMean, axisMode, axisMedian, axisHmean, axisGmean, axisStd, axisCv, axisSkew, axisKurt, axisdq = calculate_statistics(axisbankData)
hdfcData = read_excel('HDFCBANK.xlsx')
hdfcMean, hdfcMode, hdfcMedian, hdfcHmean, hdfcGmean, hdfcStd, hdfcCv, hdfcSkew, hdfcKurt, hdfcdq = calculate_statistics(hdfcData)
tcsData = read_excel('TCS.xlsx')
tcsMean, tcsMode, tcsMedian, tcsHmean, tcsGmean, tcsStd, tcsCv, tcsSkew, tcsKurt, tcsdq = calculate_statistics(tcsData)
wiproData = read_excel('WIPRO.xlsx')
wiproMean, wiproMode, wiproMedian, wiproHmean, wiproGmean, wiproStd, wiproCv, wiproSkew, wiproKurt, wiprodq = calculate_statistics(wiproData)
hclData = read_excel('HCLTECH.xlsx')
hclMean, hclMode, hclMedian, hclHmean, hclGmean, hclStd, hclCv, hclSkew, hclKurt, hcldq = calculate_statistics(hclData)

print("SBI, AXISBANK, HDFC, TCS, WIPRO, HCLTECH")
print("Mean: ", round(sbiMean, 2), round(axisMean, 2), round(hdfcMean, 2), round(tcsMean, 2), round(wiproMean, 2), round(hclMean, 2))
print("Mode: ", round(sbiMode, 2), round(axisMode, 2), round(hdfcMode, 2), round(tcsMode, 2), round(wiproMode, 2), round(hclMode, 2))
print("Median: ", round(sbiMedian, 2), round(axisMedian, 2), round(hdfcMedian, 2), round(tcsMedian, 2), round(wiproMedian, 2), round(hclMedian, 2))
print("Harmonic Mean: ", round(sbiHmean, 2), round(axisHmean, 2), round(hdfcHmean, 2), round(tcsHmean, 2), round(wiproHmean, 2), round(hclHmean, 2))
print("Geometric Mean: ", round(sbiGmean, 2), round(axisGmean, 2), round(hdfcGmean, 2), round(tcsGmean, 2), round(wiproGmean, 2), round(hclGmean, 2))
print("\n")
print("Standard Deviation: ", round(sbiStd, 2), round(axisStd, 2), round(hdfcStd, 2), round(tcsStd, 2), round(wiproStd, 2), round(hclStd, 2))
print("Coefficient of Variation: ", round(sbiCv, 2), round(axisCv, 2), round(hdfcCv, 2), round(tcsCv, 2), round(wiproCv, 2), round(hclCv, 2))
print("Skewness: ", round(sbiSkew, 2), round(axisSkew, 2), round(hdfcSkew, 2), round(tcsSkew, 2), round(wiproSkew, 2), round(hclSkew, 2))
print("Kurtosis: ", round(sbiKurt, 2), round(axisKurt, 2), round(hdfcKurt, 2), round(tcsKurt, 2), round(wiproKurt, 2), round(hclKurt, 2))
print("Data Quality", sbidq, axisdq, hdfcdq, tcsdq, wiprodq, hcldq)

# SBI, AXISBANK, HDFC, TCS, WIPRO, HCLTECH
# Mean:  569.83 1000.38 1492.02 3397.43 386.24 1274.52
# Mode:  569.25 996.22 1491.52 3374.5 382.8 1268.18
# Median:  547.0 955.45 1463.4 3330.65 378.25 1229.0
# Harmonic Mean:  569.62 999.82 1491.89 3396.18 386.1 1273.91
# Geometric Mean:  569.72 1000.1 1491.95 3396.8 386.17 1274.21


# Standard Deviation:  11.05 24.11 14.57 67.43 7.42 28.89
# Coefficient of Variation:  0.02 0.02 0.01 0.02 0.02 0.02
# Skewness:  -0.33 -0.07 -0.16 1.06 1.14 0.62
# Kurtosis:  -0.97 -1.03 -0.69 -0.39 -0.31 -0.16
# Data Quality 0.99963891201744 0.999444506663834 0.9999088193947605 0.9996309451541434 0.9996541688601999 0.9995153534656276



# Inference

# Central Tendency Measures:

# The mean, mode, median, harmonic mean, and geometric mean provide different measures of central tendency.
# For each company, the mean and median values are relatively close, suggesting that the data distribution is not highly skewed.

# Dispersion Measures:

# Standard deviation values are provided for each company, indicating the amount of variability or dispersion in the stock prices.
# All companies have relatively low standard deviations, suggesting that the stock prices are generally stable.

# Shape of the Distribution:

# Skewness is negative for SBI, AXISBANK, HDFC, and WIPRO, indicating a slight leftward skewness in their distributions.
# TCS and HCLTECH have positive skewness, suggesting a slight rightward skewness in their distributions.
# Negative kurtosis values for all companies imply that the distributions are platykurtic, meaning they have lighter tails and are less peaked than a normal distribution.

# Stock Price Relationships:

# TCS has the highest mean, median, mode, harmonic mean, and geometric mean among the listed companies, suggesting relatively higher stock prices on average.
# WIPRO has the lowest mean, median, mode, harmonic mean, and geometric mean, indicating comparatively lower stock prices on average.

# Volatility:

# TCS has the highest standard deviation, indicating higher volatility in its stock prices compared to other companies.
# HCLTECH has the lowest standard deviation, suggesting lower volatility in its stock prices.

# Data Quality:

# Data Quality is above 95% for all of the stocks. Which shows that the quality of data is good.