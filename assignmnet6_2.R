library("xlsx")
library("e1071")

# Read excel file
df <- read.xlsx("C:/Users/admin/Downloads/Crocin_Data.xlsx", sheetName = "Sheet1")


# Data is in a column named 'Data'
pre <- df$Before_Crocin
post <- df$After_Crocin

# Perform t-test
t_test_result <- t.test(pre, post, paired = TRUE)

# Extract t-value and p-value
t_value <- t_test_result$statistic
p_value <- t_test_result$p.value

print_statistics <- function(t_value, p_value) {
    cat(paste("t-value:", t_value, "\n"))
    cat(paste("p-value:", p_value, "\n"))
}

# Call the function with the statistics
print_statistics(t_value, p_value)

