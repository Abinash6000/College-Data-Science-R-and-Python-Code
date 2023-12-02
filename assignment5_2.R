library("xlsx")
library("e1071")

# Read excel file
sbi <- read.xlsx("C:/Users/admin/Downloads/SBI.xlsx", sheetName = "Sheet1")
axis <- read.xlsx("C:/Users/admin/Downloads/AXISBANK.xlsx", sheetName = "Sheet1")
hdfc <- read.xlsx("C:/Users/admin/Downloads/HDFCBANK.xlsx", sheetName = "Sheet1")
tcs <- read.xlsx("C:/Users/admin/Downloads/TCS.xlsx", sheetName = "Sheet1")
wipro <- read.xlsx("C:/Users/admin/Downloads/WIPRO.xlsx", sheetName = "Sheet1")
hcl <- read.xlsx("C:/Users/admin/Downloads/HCLTECH.xlsx", sheetName = "Sheet1")


# Data is in a column named 'Data'
sbiData <- sbi$close
axisData <- axis$close
hdfcData <- hdfc$close
tcsData <- tcs$close
wiproData <- wipro$close
hclData <- hcl$close

calculate_statistics <- function(data) {
    # Calculate statistics
    mean_value <- mean(data)
    median_value <- median(data)
    mode_value <- names(table(data))[table(data) == max(table(data))]
    std_deviation <- sd(data)
    variance_value <- var(data)
    coefficient_of_variation <- (std_deviation / mean_value) * 100
    skewness_value <- skewness(data)
    kurtosis_value <- kurtosis(data)
    
    # Return the calculated statistics as a list
    return(list(mean_value = mean_value,
                            median_value = median_value,
                            mode_value = mode_value,
                            std_deviation = std_deviation,
                            variance_value = variance_value,
                            coefficient_of_variation = coefficient_of_variation,
                            skewness_value = skewness_value,
                            kurtosis_value = kurtosis_value))
}

# Call the function with the data
sbiStatistics <- calculate_statistics(sbiData)
axisStatistics <- calculate_statistics(axisData)
hdfcStatistics <- calculate_statistics(hdfcData)
tcsStatistics <- calculate_statistics(tcsData)
wiproStatistics <- calculate_statistics(wiproData)
hclStatistics <- calculate_statistics(hclData)

# Access the calculated statistics
print_statistics <- function(statistics) {
    mean_value <- statistics$mean_value
    median_value <- statistics$median_value
    mode_value <- statistics$mode_value
    std_deviation <- statistics$std_deviation
    variance_value <- statistics$variance_value
    coefficient_of_variation <- statistics$coefficient_of_variation
    skewness_value <- statistics$skewness_value
    kurtosis_value <- statistics$kurtosis_value
    
    cat(paste("Mean:", mean_value, "\n"))
    cat(paste("Median:", median_value, "\n"))
    cat(paste("Mode:", mode_value, "\n"))
    cat(paste("Standard Deviation:", std_deviation, "\n"))
    cat(paste("Variance:", variance_value, "\n"))
    cat(paste("Coefficient of Variation:", coefficient_of_variation, "%\n"))
    cat(paste("Skewness:", skewness_value, "\n"))
    cat(paste("Kurtosis:", kurtosis_value, "\n"))
}

# Call the function with the statistics
cat(paste("\n","Sbi","\n"))
print_statistics(sbiStatistics)
cat(paste("\n","Axis","\n"))
print_statistics(axisStatistics)
cat(paste("\n","Hdfc","\n"))
print_statistics(hdfcStatistics)
cat(paste("\n","Tcs","\n"))
print_statistics(tcsStatistics)
cat(paste("\n","Wipro","\n"))
print_statistics(wiproStatistics)
cat(paste("\n","Hcl","\n"))
print_statistics(hclStatistics)
