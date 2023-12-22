library("xlsx")

# Read excel file
df <- read.xlsx("C:/Users/admin/Downloads/Auto_Sales.xlsx", sheetName = "Sheet1")
Model1 = lm(Cars_Sold~TV_Ads, data = df)

print(Model1)

set.seed(1234)
ind <- sample(2, nrow(df), replace=T, prob=c(0.8,0.2))
train <- df[ind==1,]
test <- df[ind==2,]

print(cor(train, method="pearson"))
Model1 = lm(Cars_Sold~TV_Ads, data = train)
print(Model1)

# Exploratory Data Analysis (EDA)

# plot(Cars_Sold~TV_Ads, data=df, col="red")
# boxplot(df$Cars_Sold, col='red')
# boxplot(df$TV_Ads, col='green')

print(summary(Model1))

coeff = coefficients(Model1)
print(coeff)

eq = paste("Regression Line: y =", round(coeff[1],4), "+ ", round(coeff[2],4), "*", "TV_Ads")
print(eq)

plot(Cars_Sold~TV_Ads, main=eq, data=train)
abline(Model1, col="red", lwd=2.5)