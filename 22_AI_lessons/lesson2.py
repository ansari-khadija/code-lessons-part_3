# Import LinearRegression function from Scikit-learn.linear_model
from sklearn.linear_model import LinearRegression

# sklearn → Scikit-learn library.
# linear_model → Module containing linear models.
# LinearRegression → Algorithm used for numerical predictions.

# Create a model
model = LinearRegression()

# Input data (Study hours)
X = [[1], [2], [3], [4], [5]]

# Output data (Student marks)
y = [10, 20, 30, 40, 50]

# Train the model
model.fit(X, y)

# Predict marks for a student who studies 8 hours
prediction = model.predict([[8]])

print("Model trained successfully!!")

# Display the prediction
print("Prediction for 8 hours of study:", prediction)