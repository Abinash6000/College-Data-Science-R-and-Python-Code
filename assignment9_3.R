# buff, pitt, detr


library("xlsx")

# Read excel file
df <- read.xlsx("C:/Users/admin/Downloads/data33.xlsx", sheetName = "Sheet1")

One_way <- aov(Values~Group, data = df)

cat("One-way ANOVA\n")
print(summary(One_way))