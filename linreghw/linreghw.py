import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Define data
advertising_investment = np.array([10,15,20,25,30,35,40,45,50]).reshape(-1, 1)
sales_growth = np.array([25,30,40,45,50,60,65,70,80])

# Create the model
model = LinearRegression()
model.fit(advertising_investment, sales_growth)

# Print model details
print(f"Slope (m): {model.coef_[0]:.2f}")
print(f"Intercept (b): {model.intercept_:.2f}")

# Create the equation
equation = f"y = {model.coef_[0]:.2f}x + {model.intercept_:.2f}"
print(f"Line equation: {equation}")

# Question 2
budget_to_predict  = 60
sales_result = model.coef_[0] * budget_to_predict + model.intercept_
print(f"By investing 60k the sales will be approximately {sales_result:.2f}k ILS")

# Question 3
sales_to_predict = 100
budget_result = (sales_to_predict - model.intercept_) / model.coef_[0]
print(f"To get sales growth of 100k the advertising investment should be approximately {budget_result:.2f}k ILS")

# Display the linear regression model we created above
plt.figure(figsize=(10, 6))
plt.scatter(advertising_investment, sales_growth, color='blue', label='Data points')
plt.plot(advertising_investment, model.predict(advertising_investment), color='red', label='Regression line')
plt.title('Linear Regression - Advertising Investment vs. Sales Growth')
plt.xlabel('Advertising Investment')
plt.ylabel('Sales Growth')
plt.grid(True)
plt.legend()
plt.text(25, 48, equation, fontsize=12, rotation = 30)
plt.show()