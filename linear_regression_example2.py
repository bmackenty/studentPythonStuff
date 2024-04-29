# Re-importing necessary libraries after reset
import numpy as np
import matplotlib.pyplot as plt

# Regenerating synthetic data for house sizes
house_sizes = np.arange(500, 3501, 100)  # Sizes from 500 to 3500 square feet
slope = 150  # $150 increase per square foot
intercept = 200000  # Base price of $200,000
noise = np.random.normal(0, 20000, len(house_sizes))  # Random noise to simulate real-world data

# House prices based on size plus some noise
house_prices = intercept + slope * house_sizes + noise

# Fitting a linear regression to the house price data again
house_price_coefficients = np.polyfit(house_sizes, house_prices, 1)
house_price_slope = house_price_coefficients[0]
house_price_intercept = house_price_coefficients[1]

# Generating the regression line using the fitted coefficients
house_price_regression_line = np.polyval(house_price_coefficients, house_sizes)

# Plotting the data and the regression line with slope and intercept annotated
plt.figure(figsize=(10, 6))
plt.scatter(house_sizes, house_prices, color='blue', label='Actual House Prices')
plt.plot(house_sizes, house_price_regression_line, color='red', label='Regression Line')
plt.title('Predicting House Prices Based on Size')
plt.xlabel('Size (Square Feet)')
plt.ylabel('Price ($)')
plt.text(75, 800000, f'Slope = {house_price_slope:.2f}\nIntercept = {house_price_intercept:.2f}', fontsize=12, bbox=dict(facecolor='yellow', alpha=0.5))
plt.legend()
plt.grid(True)
plt.show()

(house_price_slope, house_price_intercept)
