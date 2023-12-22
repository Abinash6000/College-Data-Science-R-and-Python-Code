# nonsmok, onepack, twopack

library("xlsx")

# Read excel file
df <- read.xlsx("C:/Users/admin/OneDrive/Desktop/VIT/Sem 4/Foundataion of Data Science/R and Python Codes/data22.xlsx", sheetName = "Sheet1")

One_way <- aov(Values~Group, data = df)

cat("One-way ANOVA\n")
print(summary(One_way))