library("xlsx")

file_path <- "C:/Users/admin/Downloads/+ve correlation 2.xlsx"
df <- read.xlsx(file_path, sheetIndex = 1)

X <- df$X
Y <- df$Y

correlation_coefficient <- cor(X, Y)
print(paste("Correlation Coefficient:", correlation_coefficient))
