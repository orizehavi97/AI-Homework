import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Create a DataFrame from our example data
columns = ['YearsExperience', 'EducationYears', 'WeeklyWorkHours', 'ManagerialExperienceYears', 'MonthlySalaryK']
data = [
    [2, 15, 40, 0, 15],
    [5, 16, 45, 1, 25],
    [3, 16, 40, 0, 18],
    [10, 18, 50, 5, 45],
    [7, 17, 45, 3, 35],
    [1, 14, 35, 0, 12],
    [8, 16, 45, 4, 38],
    [4, 15, 40, 1, 22],
    [6, 15, 42, 2, 30],
    [12, 19, 55, 8, 60]
]
df = pd.DataFrame(data, columns=columns)

# Prepare features (X) and target (y)
X = df.drop('MonthlySalaryK', axis=1)
y = df['MonthlySalaryK']

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Print model coefficients
print(f"Intercept (β₀): {model.intercept_:.2f}")
for i, col in enumerate(X.columns):
    print(f"Coefficient for {col} (β{i + 1}): {model.coef_[i]:.2f}")

# Print the prediction equation
equation = f"Salary = {model.intercept_:.2f} + " + " + ".join(
    [f"{model.coef_[i]:.2f}*{col}" for i, col in enumerate(X.columns)]
)
print(f"\nPrediction equation: {equation}")

# Make a prediction for a new worker
new_worker = pd.DataFrame([[6, 16, 43, 2]], columns=X.columns)
predicted_salary = model.predict(new_worker)[0]
print(f"\nPredicted salary for the new worker: {predicted_salary:.2f} thousand ILS")

# The most influential variables on the salary are in this order:
# 1. ManagerialExperienceYears
# 2. YearsExperience
# 3. EducationYears
# 4. WeeklyWorkHours
# The higher the coefficient, the bigger its influence on the salary will be
