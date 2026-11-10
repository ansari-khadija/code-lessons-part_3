
# Import required libraries
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Input data (Study hours)
X = [[1], [2], [3], [4], [5],
     [6], [7], [8], [9], [10]]

# Output data (0 = Fail, 1 = Pass)
y = [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]


# PART 1: Understand accuracy_score separately

# Actual answers
y_actual = [1, 0, 1, 1, 0]

# Model predictions
y_predicted = [1, 0, 0, 1, 0]

# Calculate accuracy
accuracy = accuracy_score(y_actual, y_predicted)

print("Manual Accuracy:", accuracy)
print("Manual Accuracy Percentage:", accuracy * 100, "%")


# PART 2: Train Decision Tree model

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,      # 20% testing and 80% training
    random_state=42    # Keep the split consistent
)

# Create Decision Tree model
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Calculate model accuracy
accuracy = accuracy_score(y_test, y_pred)

print("Actual Results:", y_test)
print("Predicted Results:", y_pred)
print("Model Accuracy:", accuracy * 100, "%")
