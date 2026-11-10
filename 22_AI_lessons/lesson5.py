
# Import Linear Regression
from sklearn.linear_model import LinearRegression

# Input dataset with THREE features
# Study hours, Sleep hours, Attendance
X = [
    [2, 8, 80],
    [4, 7, 85],
    [6, 8, 90],
    [8, 7, 95],
    [10, 8, 100]
]

# Target/output: Student marks
y = [30, 45, 65, 80, 95]

# Create Linear Regression model
model = LinearRegression()

# Train the model
model.fit(X, y)

# Display coefficients
print("Coefficients:", model.coef_)

# Display intercept
print("Intercept:", model.intercept_)

# Predict marks for a new student
# Study hours = 5
# Sleep hours = 8
# Attendance = 90
new_student = [[5, 8, 90]]

prediction = model.predict(new_student)

print("Predicted Marks:", prediction[0])
