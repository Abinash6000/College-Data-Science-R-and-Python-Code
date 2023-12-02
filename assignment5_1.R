install.packages("xlsx")
install.packages("e1071")

library("xlsx")
library("e1071")

# Read excel file
df <- read.xlsx("C:/Users/admin/Downloads/PartyDataset.xlsx", sheetName = "Sheet1")


# Data is in a column named 'Data'
data <- df$Data

# Calculate statistics
mean_value <- mean(data)
median_value <- median(data)
mode_value <- names(table(data))[table(data) == max(table(data))]
std_deviation <- sd(data)
variance_value <- var(data)
coefficient_of_variation <- (std_deviation / mean_value) * 100
skewness_value <- skewness(data)
kurtosis_value <- kurtosis(data)

print_statistics <- function(mean_value, median_value, mode_value, std_deviation, variance_value, coefficient_of_variation, skewness_value, kurtosis_value) {
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
print_statistics(mean_value, median_value, mode_value, std_deviation, variance_value, coefficient_of_variation, skewness_value, kurtosis_value)

