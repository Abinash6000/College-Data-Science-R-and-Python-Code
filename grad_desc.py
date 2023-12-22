import numpy as np
import matplotlib.pyplot as plt

# Given data
x = np.array([1400, 1600, 1700, 1875, 1100, 1550, 2350, 2450, 1425, 1700])
y = np.array([245000, 312000, 279000, 308000, 199000, 219000, 405000, 324000, 319000, 255000])




# Initialize parameters
learning_rate = 0.0000001
iterations = 101
m = len(x)

# Initialize weights (slope) and bias (intercept)
w = 0
b = 0

# Perform gradient descent
for i in range(iterations):
    # Predicted values
    y_pred = w * x + b
    
    # Calculate gradients
    dw = (1/m) * np.sum((y_pred - y) * x)
    db = (1/m) * np.sum(y_pred - y)
    
    # Update weights and bias
    w = w - learning_rate * dw
    b = b - learning_rate * db
    
    # Calculate cost (mean squared error)
    cost = (1/(2*m)) * np.sum((y_pred - y)**2)
    
    # Print progress every 1 iterations
    print(f'Iteration {i}, Cost: {cost}, w: {w}, b: {b}')
    # print(f'Iteration {i}, b: {b}, w: {w}')

# Plot the data and the regression line
# plt.scatter(x, y, label='Original data')
# plt.plot(x, w * x + b, color='red', label='Regression line')
# plt.xlabel('x')
# plt.ylabel('y')
# plt.legend()
# plt.show()
