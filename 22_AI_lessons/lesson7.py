
# Import required libraries
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Create input dataset
# Study hours and attendance
X = [
    [5, 80],
    [6, 90],
    [8, 95],
    [4, 70],
    [7, 85],
    [9, 98],
    [3, 65],
    [10, 100]
]

# Create target/output dataset
# Student marks
y = [50, 60, 80, 40, 70, 90, 30, 95]


# STEP 1: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42
)


# STEP 2: Create StandardScaler
scaler = StandardScaler()

# Learn scaling information from training data
# Then scale training data
X_train_scaled = scaler.fit_transform(X_train)

# Scale testing data using training statistics
X_test_scaled = scaler.transform(X_test)


# STEP 3: Create Linear Regression model
model = LinearRegression()

# Train model using scaled training data
model.fit(X_train_scaled, y_train)


# STEP 4: Make predictions
y_pred = model.predict(X_test_scaled)

print("Actual Marks:", y_test)
print("Predicted Marks:", y_pred)


# STEP 5: Evaluate model
mse = mean_squared_error(y_test, y_pred)

print("Mean Squared Error:", mse)
