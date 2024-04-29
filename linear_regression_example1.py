import numpy as np
import matplotlib.pyplot as plt

# Generating synthetic data
np.random.seed(0)
years_of_experience = np.arange(0, 21)  # Years from 0 to 20
slope = 3000  # $3000 increase per year
intercept = 40000  # Starting salary of $40,000
noise = np.random.normal(0, 5000, len(years_of_experience))  # Random noise

# Salary based on years of experience plus some noise
salaries = intercept + slope * years_of_experience + noise

# Fitting a linear regression
coefficients = np.polyfit(years_of_experience, salaries, 1)
regression_line = np.polyval(coefficients, years_of_experience)


# Fitting a linear regression to the salary data
salary_coefficients = np.polyfit(years_of_experience, salaries, 1)
salary_slope = salary_coefficients[0]
salary_intercept = salary_coefficients[1]

# Generating the regression line using the fitted coefficients
salary_regression_line = np.polyval(salary_coefficients, years_of_experience)




# Plotting the data and the regression line
plt.figure(figsize=(10, 6))
plt.scatter(years_of_experience, salaries, color='blue', label='Actual Salaries')
plt.plot(years_of_experience, regression_line, color='red', label='Regression Line')
plt.title('Predicting Salary Based on Years of Experience')
plt.xlabel('Years of Experience')
plt.ylabel('Salary ($)')
plt.text(17, 100000, f'Slope = {salary_slope:.2f}\nIntercept = {salary_intercept:.2f}', fontsize=12, bbox=dict(facecolor='yellow', alpha=0.5))
plt.legend()
plt.grid(True)
plt.show()
