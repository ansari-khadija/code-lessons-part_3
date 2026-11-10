# importing mean_squared_error from sklearn.metrics
from sklearn.metrics import mean_squared_error

# Import LinearRegression function from Scikit-learn.linear_model
from sklearn.linear_model import LinearRegression

# Create dataset
X = [[1], [2], [3], [4], [5]]
y = [10, 20, 30, 40, 50]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Make predictions on the same data
y_pred = model.predict(X)

# Calculate Mean Squared Error
# Formula: MSE= n∑(y−y_pred)^2
mse = mean_squared_error(y, y_pred)

# Display result
print("Actual values:", y)
print("Predicted values:", y_pred)
print("MSE:", mse)
print("Mean Squared Error:", mse)
print("MSE rounded:", round(mse, 2))