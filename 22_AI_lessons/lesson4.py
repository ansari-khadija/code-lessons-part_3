
# Import Linear Regression
from sklearn.linear_model import LinearRegression

# Create input data
X = [[1], [2], [3], [4], [5]]

# Create output data
y = [10, 20, 30, 40, 50]

# Create model
model = LinearRegression()

# Train model
model.fit(X, y)

# Get coefficient (slope)
print("Coefficient:", model.coef_)

# Get intercept
print("Intercept:", model.intercept_)

# Predict marks for 6 study hours
prediction = model.predict([[6]])

print("Predicted Marks:", prediction[0])
