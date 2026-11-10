# Import pandas to create and manage datasets
import pandas as pd

# Import function to split dataset into training and testing data
from sklearn.model_selection import train_test_split

# Import Linear Regression algorithm
from sklearn.linear_model import LinearRegression

# Import Mean Squared Error to evaluate model performance
from sklearn.metrics import mean_squared_error

# Create a dataset containing study hours and student marks
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Marks": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
}

# Convert dictionary into a Pandas DataFrame
df = pd.DataFrame(data)

# Display dataset
print(df)
# X = Input feature (study hours)
X = df[["Hours"]]

# y = Target/output (student marks)
y = df["Marks"]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,      # 20% testing and 80% training
    random_state=42     # Keep the split consistent
)

# Display training and testing data
print("Training inputs:", X_train)
print("Testing inputs:", X_test)

# Create Linear Regression model
model = LinearRegression()

# Train the model using training data
model.fit(X_train, y_train)

print("Model trained successfully!")

# Predict marks using testing input data
y_pred = model.predict(X_test)

# Display actual and predicted marks
print("Actual Marks:", y_test.tolist())
print("Predicted Marks:", y_pred)

# Calculate Mean Squared Error using testing data
mse = mean_squared_error(y_test, y_pred)

print("Model MSE:", mse)

# A new student studies for 7 hours
new_student = pd.DataFrame({
    "Hours": [7]
})

# Predict the student's marks
result = model.predict(new_student)

print("Predicted Marks:", result[0])